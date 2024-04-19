import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from House import House, RunSimulation, PlotBaseCase, PlotScenario, PV

# ------------------ Data import -----------------

T2M_2019_ZRH = pd.read_csv(r"ren_ninja/CHE/T2M_2019_ZRH.csv", delimiter=",", header=3)["t2m"].tolist()
T2M_2019_MAD = pd.read_csv(r"ren_ninja/ESP/T2M_2019_MAD.csv", delimiter=",", header=3)["t2m"].tolist()
T2M_2019_BAR = pd.read_csv(r"ren_ninja/ESP/T2M_2019_BAR.csv", delimiter=",", header=3)["t2m"].tolist()
T2M_2019_STO = pd.read_csv(r"ren_ninja/SWE/T2M_2019_STO.csv", delimiter=",", header=3)["t2m"].tolist()
T2M_2019_SOF = pd.read_csv(r"ren_ninja/BUL/T2M_2019_SOF.csv", delimiter=",", header=3)["t2m"].tolist()

IRRADIATION_2019_ZRH = pd.read_csv(r"ren_ninja/CHE/IRR_2019_ZRH.csv", delimiter=",", header=3)["swgdn"].tolist()
IRRADIATION_2019_MAD = pd.read_csv(r"ren_ninja/ESP/IRR_2019_MAD.csv", delimiter=",", header=3)["swgdn"].tolist()
IRRADIATION_2019_BAR = pd.read_csv(r"ren_ninja/ESP/IRR_2019_BAR.csv", delimiter=",", header=3)["swgdn"].tolist()
IRRADIATION_2019_STO = pd.read_csv(r"ren_ninja/SWE/IRR_2019_STO.csv", delimiter=",", header=3)["swgdn"].tolist()
IRRADIATION_2019_SOF = pd.read_csv(r"ren_ninja/BUL/IRR_2019_SOF.csv", delimiter=",", header=3)["swgdn"].tolist()

# convert to kelvin
T_OUTSIDE_2019_ZRH = [temp + 273.15 for temp in T2M_2019_ZRH]
T_OUTSIDE_2019_MAD = [temp + 273.15 for temp in T2M_2019_MAD]
T_OUTSIDE_2019_BAR = [temp + 273.15 for temp in T2M_2019_BAR]
T_OUTSIDE_2019_STO = [temp + 273.15 for temp in T2M_2019_STO]
T_OUTSIDE_2019_SOF = [temp + 273.15 for temp in T2M_2019_SOF]

PV_GEN_2019_CHE = PV("PV_data/Hourly_electricity_per_area_Switzerland.csv").get()
PV_GEN_2019_ESP = PV("PV_data/Hourly_electricity_per_area_Spain.csv").get()
PV_GEN_2019_SWE = PV("PV_data/Hourly_electricity_per_area_Sweden.csv").get()
PV_GEN_2019_BUL = PV("PV_data/Hourly_electricity_per_area_Bulgaria.csv").get()



# ------------- Import defined house parameters -----------

from parameters import CHE_HOUSE_TYPES, ESP_HOUSE_TYPES, SWE_HOUSE_TYPES, BUL_HOUSE_TYPES
from parameters import ONLY_MFH_BEFORE_2000_CHE
from parameters import SETPOINT_AC_CH, SETPOINT_HP_CH, SETPOINT_AC_ESP, SETPOINT_HP_ESP, SETPOINT_AC_SWE, SETPOINT_HP_SWE, SETPOINT_AC_BUL, SETPOINT_HP_BUL 

#-------------- Initialize simulation objects -----------------

SCENARIO_CH_TEMP = {}

CHE_HOUSE_SIMULATION = {}
ESP_HOUSE_SIMULATION = {}
SWE_HOUSE_SIMULATION = {}
BUL_HOUSE_SIMULATION = {}

# -------------------- Define Scenarios ----------------------

y_start = 2020  # Starting year
y_end = 2050    # Ending year
y_step = 5      # Calculate every X year
t_inc = 0.05    # Yearly temperature increase

y_range = range(y_start, y_end+1, y_step) 
t_develop = [0] + [t_inc*y_step] * (len(y_range)-1)

GLOBAL_TEMPERATURE_SCENARIO = {
    "years": y_range,
    "temp_develop": t_develop}

uvalue_years = [1970, 2030]

CHE_UVALUE_SCENARIO = {
    "years": uvalue_years,
    "U_wall": [0.6, 0.2],
    "U_window": [2.7, 1.2],
    "U_floor": [1.2, 0.3],
    "shgc": [0.7, 0.2]
}
#-------------- Auxiliary functions ------------

def simulate_country(house_types, t_outside, pv_prod, irradiation):
    output = {}
    for house, params in house_types.items():
        output[house] = RunSimulation(House(**params), pv_prod, irradiation, 3600).run(t_outside)
    return output

def simulate_temp_scenario(house_types, t_outside, pv_prod, irradiation, scenario, specific_house):
    output = {}
    temp = {}
    for house_types, params in house_types.items():
        temp[house_types] = RunSimulation(House(**params), pv_prod, irradiation, 3600, scenario)
    output = temp[specific_house].run_scenario_temp(t_outside)
    return output

def simulate_uvalue_scenario(house_types, t_outside, pv_prod, irradiation, scenario, specific_house):
    output = {}
    temp = {}
    for house_types, params in house_types.items():
        temp[house_types] = RunSimulation(House(**params), pv_prod, irradiation, 3600, scenario)
    output = temp[specific_house].run_scenario_uvalue(t_outside)
    return output

def print_stats(output_dict, country):
    for house, _ in output_dict.items():
        print(f'{country}')
        print("Statistic for:", house, '\n')
        print(f'Total Electricity produced with PV for {house}: {round(sum(output_dict[house][6]) / 1e3, 2)} [kWh]')
        print(f'Average temperature inside {house}: {round(np.mean(output_dict[house][0]), 2)} [K]')
        print(f'Electricity needed for cooling of {house}: {round(sum(output_dict[house][1]) / (3.5 * 1e3), 2)} [kWh]')
        print(f'Electricity needed for heating of {house}: {round(sum(output_dict[house][5]) / (3.5 * 1e3), 2)} [kWh]')
        print(f'Net Cooling Demand {house}: {round(sum(output_dict[house][4]) / (3.5 * 1e3), 2)} [kWh] \n')
        print('\n')


#------------ Perform calculations of sim object ------------------

CHE_HOUSE_SIMULATION = simulate_country(CHE_HOUSE_TYPES, T_OUTSIDE_2019_ZRH, PV_GEN_2019_CHE, IRRADIATION_2019_ZRH)
# ESP_HOUSE_SIMULATION = simulate_country(ESP_HOUSE_TYPES, T_OUTSIDE_2019_MAD, PV_GEN_2019_ESP, IRRADIATION_2019_MAD)
# SWE_HOUSE_SIMULATION = simulate_country(SWE_HOUSE_TYPES, T_OUTSIDE_2019_STO, PV_GEN_2019_SWE, IRRADIATION_2019_STO)
# BUL_HOUSE_SIMULATION = simulate_country(BUL_HOUSE_TYPES, T_OUTSIDE_2019_SOF, PV_GEN_2019_BUL, IRRADIATION_2019_SOF)

# test_sim = simulate_country(ONLY_MFH_BEFORE_2000_CHE, T_OUTSIDE_2019_MAD, PV_GEN_2019_ESP, IRRADIATION_2019_MAD)
# test_sim_plot = PlotBaseCase(test_sim)
# test_sim_plot.plt_supply_vs_demand(168)
# test_sim_plot.plt_ac_consumption()
# test_sim_plot.plt_t_inside(168, SETPOINT_AC_CH, SETPOINT_HP_CH)

print_stats(CHE_HOUSE_SIMULATION, 'SWITZERLAND')
# print_stats(ESP_HOUSE_SIMULATION, 'SPAIN')
# print_stats(SWE_HOUSE_SIMULATION, 'SWEDEN')
# print_stats(BUL_HOUSE_SIMULATION, 'BULGARIA')

SCENARIO_CH_TEMP = simulate_uvalue_scenario(CHE_HOUSE_TYPES, T_OUTSIDE_2019_ZRH, PV_GEN_2019_CHE, IRRADIATION_2019_ZRH, CHE_UVALUE_SCENARIO, "MFH after 2000")

test = PlotScenario(SCENARIO_CH_TEMP, PV_GEN_2019_CHE, "MFH after 2000")
test.plt_t_inside(SETPOINT_AC_CH, SETPOINT_HP_CH)
test.plt_scenario_ac_demand()
test.plt_scenario_net_demand()
test.plt_scenario_battery_flow()
test.plt_scenario_soc()
test.plt_scenario_hp_demand()


# ------------ Perform calculations of sim object ------------------

   

#------------ Initialize plotting objects ----------------
"""
#TODO generate PV_GEN for different countries
CHE_PLOTS = Plot_output(CHE_HOUSE_SIMULATION, PV_GEN_2019_ZRH)
ESP_PLOTS = Plot_output(ESP_HOUSE_SIMULATION, PV_GEN_2019_ZRH)
SWE_PLOTS = Plot_output(SWE_HOUSE_SIMULATION, PV_GEN_2019_ZRH)
BUL_PLOTS = Plot_output(BUL_HOUSE_SIMULATION, PV_GEN_2019_ZRH)

CHE_PLOTS.plt_net_demand()
CHE_PLOTS.plt_SOC_battery(168)
CHE_PLOTS.plt_ac_consumption()
CHE_PLOTS.plt_t_inside(168, SETPOINT_AC_CH, SETPOINT_HP_CH)
CHE_PLOTS.bar_plot_ac_consumption()
CHE_PLOTS.bar_plot_net_demand()

ESP_PLOTS.plt_net_demand()
ESP_PLOTS.plt_SOC_battery(168)
ESP_PLOTS.plt_ac_consumption()
ESP_PLOTS.plt_t_inside(168, SETPOINT_AC_ESP, SETPOINT_HP_ESP)
ESP_PLOTS.bar_plot_ac_consumption()
ESP_PLOTS.bar_plot_net_demand()

SWE_PLOTS.plt_net_demand()
SWE_PLOTS.plt_SOC_battery(168)
SWE_PLOTS.plt_ac_consumption()
SWE_PLOTS.plt_t_inside(168, SETPOINT_AC_SWE, SETPOINT_HP_SWE)
SWE_PLOTS.bar_plot_ac_consumption()
SWE_PLOTS.bar_plot_net_demand()

BUL_PLOTS.plt_net_demand()
BUL_PLOTS.plt_SOC_battery(168)
BUL_PLOTS.plt_ac_consumption()
BUL_PLOTS.plt_t_inside(168, SETPOINT_AC_BUL, SETPOINT_HP_BUL)
BUL_PLOTS.bar_plot_ac_consumption()
BUL_PLOTS.bar_plot_net_demand()

# plots = Plot_output(scenario_output, PV_GEN_2019_ZRH)
# plots.plot_temperature_scenario(168)
# plots.plot_ac_demand()
# plots.plot_aggregated_ac_demand_over_years()
# plots.plot_base_case_with_PV()

# print(f'Cooling needed for old MFH: {round(sum((comparison_output['old_MFH'][1])) / (3.5 * 1e3), 2)} [kWh]')
# print(f'Heating needed for old MFH: {round(sum(comparison_output['old_MFH'][5]) / (3.5 * 1e3), 2)} [kWh] \n')

# print(f'Cooling needed for old SFH: {round(sum((comparison_output['old_SFH'][1])) / (3.5 * 1e3), 2)} [kWh]')
# print(f'Heating needed for old SFH: {round(sum(comparison_output['old_SFH'][5]) / (3.5 * 1e3), 2)} [kWh] \n')

# print(f'Total electricity with Battery for old SFH: {round(comparison_output['old_SFH'][6]) / 1e6} [MW]')
# print(f'Cooling needed for old SFH: {round(comparison_output['old_SFH'][2]) / 1e6} [MW]')

# print(f'Total electricity with Battery for modern MFH: {round(comparison_output['modern_MFH'][6]) / 1e6} [MW]')
# print(f'Cooling needed for modern MFH: {round(comparison_output['modern_MFH'][2]) / 1e6} [MW]')

# print(f'Total electricity with Battery for modern SFH: {round(comparison_output['modern_SFH'][6]) / 1e6} [MW]')
# print(f'Cooling needed for modern SFH: {round(comparison_output['modern_SFH'][2]) / 1e6} [MW]')

"""

