import pandas as pd
import numpy as np

# ------------------ Data import -----------------

T2M_2019_ZRH = pd.read_csv(r"ren_ninja/CHE/T2M_2019_ZRH.csv", delimiter=",", header=3)["t2m"].tolist() # Zurich
T2M_2019_MAD = pd.read_csv(r"ren_ninja/ESP/T2M_2019_MAD.csv", delimiter=",", header=3)["t2m"].tolist() # Madrid
T2M_2019_BAR = pd.read_csv(r"ren_ninja/ESP/T2M_2019_BAR.csv", delimiter=",", header=3)["t2m"].tolist() # Barcelona
T2M_2019_STO = pd.read_csv(r"ren_ninja/SWE/T2M_2019_STO.csv", delimiter=",", header=3)["t2m"].tolist() # Stockholm
T2M_2019_SOF = pd.read_csv(r"ren_ninja/BUL/T2M_2019_SOF.csv", delimiter=",", header=3)["t2m"].tolist() # Sofia

IRRADIATION_2019_ZRH = pd.read_csv(r"ren_ninja/CHE/IRR_2019_ZRH.csv", delimiter=",", header=3)["swgdn"].tolist() # Zurich
IRRADIATION_2019_MAD = pd.read_csv(r"ren_ninja/ESP/IRR_2019_MAD.csv", delimiter=",", header=3)["swgdn"].tolist() # Madrid
IRRADIATION_2019_BAR = pd.read_csv(r"ren_ninja/ESP/IRR_2019_BAR.csv", delimiter=",", header=3)["swgdn"].tolist() # Barcelona
IRRADIATION_2019_STO = pd.read_csv(r"ren_ninja/SWE/IRR_2019_STO.csv", delimiter=",", header=3)["swgdn"].tolist() # Stockholm
IRRADIATION_2019_SOF = pd.read_csv(r"ren_ninja/BUL/IRR_2019_SOF.csv", delimiter=",", header=3)["swgdn"].tolist() # Sofia

# convert to kelvin
T_OUTSIDE_2019_ZRH = [temp + 273.15 for temp in T2M_2019_ZRH]
T_OUTSIDE_2019_MAD = [temp + 273.15 for temp in T2M_2019_MAD]
T_OUTSIDE_2019_BAR = [temp + 273.15 for temp in T2M_2019_BAR]
T_OUTSIDE_2019_STO = [temp + 273.15 for temp in T2M_2019_STO]
T_OUTSIDE_2019_SOF = [temp + 273.15 for temp in T2M_2019_SOF]


# ------------- Import defined house parameters -----------

from parameters import CHE_HOUSE_TYPES, ESP_HOUSE_TYPES, SWE_HOUSE_TYPES, BUL_HOUSE_TYPES
from parameters import CHE_OLD_MFH, ESP_OLD_MFH, SWE_OLD_MFH, BUL_OLD_MFH
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

uvalue_years = [1970, 2000, 2030]

CHE_UVALUE_SCENARIO = {
    "years": uvalue_years,
    "U_wall": [0.6, 0.4, 0.2],
    "U_window": [2.7, 1.8, 1.2],
    "U_floor": [1.2, 0.7, 0.3],
    "shgc": [0.7, 0.45, 0.2]
}
#-------------- Auxiliary functions ------------

from House import House, RunSimulation, PlotBaseCase, PlotScenario

def simulate_house(house_types, t_outside, irradiation):
    output = {}
    for house, params in house_types.items():
        output[house] = RunSimulation(House(**params), irradiation, 3600).run(t_outside)
    return output

def simulate_temp_scenario(house_types, t_outside, irradiation, scenario, specific_house):
    output = {}
    temp = {}
    for house_types, params in house_types.items():
        temp[house_types] = RunSimulation(House(**params), irradiation, 3600, scenario)
    output = temp[specific_house].run_scenario_temp(t_outside)
    return output

def simulate_uvalue_scenario(house_types, t_outside, irradiation, scenario, specific_house):
    output = {}
    temp = {}
    for house_types, params in house_types.items():
        temp[house_types] = RunSimulation(House(**params), irradiation, 3600, scenario)
    output = temp[specific_house].run_scenario_uvalue(t_outside)
    return output

def variance(input_list):
    n = len(input_list)
    mean = sum(input_list) / n
    variance = sum((x - mean) ** 2 for x in input_list) / n
    return variance

def print_stats(output_dict, country):
    for house, _ in output_dict.items():
        print(f'{country}')
        print("Statistic for:", house, '\n')
        print(f'Total Electricity produced with PV for {house}: {round(sum(output_dict[house][6]) / 1e3, 2)} [kWh]')
        print(f'Average temperature inside {house}: {round(np.mean(output_dict[house][0]), 2)} [K]')
        print(f'Std. deviation inside Temperature of {house}: {round(np.sqrt(variance(output_dict[house][0])), 2)} [K]')
        print(f'Electricity needed for cooling of {house}: {round(sum(output_dict[house][1]) / (3.5 * 1e3), 2)} [kWh]')
        print(f'Electricity needed for heating of {house}: {round(sum(output_dict[house][5]) / (3.5 * 1e3), 2)} [kWh]')
        print(f'Net Cooling Demand {house}: {round(sum(output_dict[house][4]) / (3.5 * 1e3), 2)} [kWh] \n')
        print('\n')


#------------ Perform calculations of sim object ------------------

CHE_HOUSES_SIMULATION = simulate_house(CHE_HOUSE_TYPES, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH)
ESP_HOUSES_SIMULATION = simulate_house(ESP_HOUSE_TYPES, T_OUTSIDE_2019_MAD, IRRADIATION_2019_MAD)
SWE_HOUSES_SIMULATION = simulate_house(SWE_HOUSE_TYPES, T_OUTSIDE_2019_STO, IRRADIATION_2019_STO)
BUL_HOUSES_SIMULATION = simulate_house(BUL_HOUSE_TYPES, T_OUTSIDE_2019_SOF, IRRADIATION_2019_SOF)

CHE_OLD_MFH_SIMULATION = simulate_house(CHE_OLD_MFH, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH)
ESP_OLD_MFH_SIMULATION = simulate_house(ESP_OLD_MFH, T_OUTSIDE_2019_MAD, IRRADIATION_2019_MAD)
SWE_OLD_MFH_SIMULATION = simulate_house(SWE_OLD_MFH, T_OUTSIDE_2019_STO, IRRADIATION_2019_STO)
BUL_OLD_MFH_SIMULATION = simulate_house(BUL_OLD_MFH, T_OUTSIDE_2019_SOF, IRRADIATION_2019_SOF)

# -------------- Initialize Plotting objects ------------------------

CHE_COMPARE_PLOT = PlotBaseCase(CHE_HOUSES_SIMULATION)
ESP_COMPARE_PLOT = PlotBaseCase(ESP_HOUSES_SIMULATION)
SWE_COMPARE_PLOT = PlotBaseCase(SWE_HOUSES_SIMULATION)
BUL_COMPARE_PLOT = PlotBaseCase(BUL_HOUSES_SIMULATION)

CHE_SINGLE_PLOT = PlotBaseCase(CHE_OLD_MFH_SIMULATION)
ESP_SINGLE_PLOT = PlotBaseCase(ESP_OLD_MFH_SIMULATION)
SWE_SINGLE_PLOT = PlotBaseCase(SWE_OLD_MFH_SIMULATION)
BUL_SINGLE_PLOT = PlotBaseCase(BUL_OLD_MFH_SIMULATION)

# ---------------------- Plot output --------------------------

avg_window = 168

CHE_SINGLE_PLOT.plt_supply_vs_demand(avg_window)

print_stats(CHE_HOUSES_SIMULATION, 'SWITZERLAND')

#SCENARIO_CH_TEMP = simulate_uvalue_scenario(CHE_HOUSE_TYPES, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, CHE_UVALUE_SCENARIO, "MFH after 2000")

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

