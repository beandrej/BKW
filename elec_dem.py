import pandas as pd
import numpy as np

# ------------------ Data import -----------------

T2M_2019_ZRH = pd.read_csv(r"ren_ninja/CHE/T2M_2019_ZRH.csv", delimiter=",", header=3)["t2m"].tolist() # Zurich
T2M_2019_MAD = pd.read_csv(r"ren_ninja/ESP/T2M_2019_MAD.csv", delimiter=",", header=3)["t2m"].tolist() # Madrid
T2M_2019_BAR = pd.read_csv(r"ren_ninja/ESP/T2M_2019_BAR.csv", delimiter=",", header=3)["t2m"].tolist() # Barcelona
T2M_2019_STO = pd.read_csv(r"ren_ninja/SWE/T2M_2019_STO.csv", delimiter=",", header=3)["t2m"].tolist() # Stockholm
T2M_2019_SOF = pd.read_csv(r"ren_ninja/BUL/T2M_2019_SOF.csv", delimiter=",", header=3)["t2m"].tolist() # Sofia
T2M_2019_HAM = pd.read_csv(r"ren_ninja/DE/2019_Hamburg.csv", delimiter=",", header=3)["t2m"].tolist() # Hamburg
T2M_2019_PAR = pd.read_csv(r"ren_ninja/FR/2019_Paris.csv", delimiter=",", header=3)["t2m"].tolist() # Paris
T2M_2019_ROM = pd.read_csv(r"ren_ninja/IT/2019_Rome.csv", delimiter=",", header=3)["t2m"].tolist() # Rome

IRRADIATION_2019_ZRH = pd.read_csv(r"ren_ninja/CHE/IRR_2019_ZRH.csv", delimiter=",", header=3)["swgdn"].tolist() # Zurich
IRRADIATION_2019_MAD = pd.read_csv(r"ren_ninja/ESP/IRR_2019_MAD.csv", delimiter=",", header=3)["swgdn"].tolist() # Madrid
IRRADIATION_2019_BAR = pd.read_csv(r"ren_ninja/ESP/IRR_2019_BAR.csv", delimiter=",", header=3)["swgdn"].tolist() # Barcelona
IRRADIATION_2019_STO = pd.read_csv(r"ren_ninja/SWE/IRR_2019_STO.csv", delimiter=",", header=3)["swgdn"].tolist() # Stockholm
IRRADIATION_2019_SOF = pd.read_csv(r"ren_ninja/BUL/IRR_2019_SOF.csv", delimiter=",", header=3)["swgdn"].tolist() # Sofia
IRRADIATION_2019_HAM = pd.read_csv(r"ren_ninja/DE/2019_Hamburg.csv", delimiter=",", header=3)["swgdn"].tolist() # Hamburg
IRRADIATION_2019_PAR = pd.read_csv(r"ren_ninja/FR/2019_Paris.csv", delimiter=",", header=3)["swgdn"].tolist() # Paris
IRRADIATION_2019_ROM = pd.read_csv(r"ren_ninja/IT/2019_Rome.csv", delimiter=",", header=3)["swgdn"].tolist() # Rome

# convert to kelvin
T_OUTSIDE_2019_ZRH = [temp + 273.15 for temp in T2M_2019_ZRH]
T_OUTSIDE_2019_MAD = [temp + 273.15 for temp in T2M_2019_MAD]
T_OUTSIDE_2019_BAR = [temp + 273.15 for temp in T2M_2019_BAR]
T_OUTSIDE_2019_STO = [temp + 273.15 for temp in T2M_2019_STO]
T_OUTSIDE_2019_SOF = [temp + 273.15 for temp in T2M_2019_SOF]
T_OUTSIDE_2019_HAM = [temp + 273.15 for temp in T2M_2019_HAM]
T_OUTSIDE_2019_PAR = [temp + 273.15 for temp in T2M_2019_PAR]
T_OUTSIDE_2019_ROM = [temp + 273.15 for temp in T2M_2019_ROM]


# ------------- Import defined house parameters -----------

from parameters import CHE_HOUSE_TYPES, ESP_HOUSE_TYPES, SWE_HOUSE_TYPES, BUL_HOUSE_TYPES, IT_HOUSE_TYPES, DE_HOUSE_TYPES,FR_HOUSE_TYPES
from parameters import CHE_OLD_MFH, ESP_OLD_MFH, SWE_OLD_MFH, BUL_OLD_MFH, IT_OLD_MFH, DE_OLD_MFH, FR_OLD_MFH
from parameters import CHE_NEW_SFH, ESP_NEW_SFH
from parameters import SETPOINT_AC_CH, SETPOINT_HP_CH, SETPOINT_AC_ESP, SETPOINT_HP_ESP, SETPOINT_AC_SWE, SETPOINT_HP_SWE, SETPOINT_AC_BUL, SETPOINT_HP_BUL, SETPOINT_AC_FR,SETPOINT_HP_FR,SETPOINT_AC_DE,SETPOINT_HP_DE,SETPOINT_AC_IT,SETPOINT_HP_IT

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
        output[house] = RunSimulation(House(**params), t_outside, irradiation, 3600).run(t_outside)
    return output

def simulate_temp_scenario(house_types, t_outside, irradiation, scenario, specific_house):
    output = {}
    temp = {}
    for house_types, params in house_types.items():
        temp[house_types] = RunSimulation(House(**params), t_outside, irradiation, 3600, scenario)
    output = temp[specific_house].run_scenario_temp(t_outside)
    return output

def simulate_uvalue_scenario(house_types, t_outside, irradiation, scenario):
    output = {}
    temp = {}
    for house_types, params in house_types.items():
        temp[house_types] = RunSimulation(House(**params), t_outside, irradiation, 3600, scenario)
        output[f'{house_types}'] = temp[house_types].run_scenario_uvalue(t_outside)
    return output





def simulate_sensitivity_analysis (house_types, t_outside, irradiation, list_of_parameters, list_range):
    output = {}
    for house in house_types.keys():
        output_dictionary = {}
        for param in list_of_parameters:
            copy_house = house_types[house].copy()
            list_output = []
            for multiplier in list_range:
                if type(param) ==list:
                    for sub_param in param:
                        copy_house[sub_param] = house_types[house][sub_param] * multiplier
                else:
                   copy_house[param] = house_types[house][param] * multiplier
                list_output += [np.sum(RunSimulation(House(**copy_house), irradiation, 3600).run(t_outside)[1])]
            if type(param) == list:
                output_dictionary[param[0] + ' +others'] = list_output
            else:
                output_dictionary[param] = list_output
        output[house] = output_dictionary
    return output

def simulate_sensitivity_temperature_setpoint(house_types, t_outside, irradiation, list_of_temperatures):
    output = {}
    for house in house_types.keys():
        output_demand= []
        for temp in list_of_temperatures:
            copy_house = house_types[house].copy()
            copy_house['setpoint_ac'] = temp
            if temp<=293:
                copy_house['setpoint_hp'] = temp-1
            else:
                copy_house['setpoint_hp'] = 293
            output_demand += [np.sum(RunSimulation(House(**copy_house), irradiation, 3600).run(t_outside)[1])]
        output[house] = output_demand
    print(output)
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

#------------ Sensitivity Analysis ------------------
"""
CHE_HOUSES_SENSITIVITY = simulate_sensitivity_analysis(CHE_HOUSE_TYPES, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, [['U_wall', 'U_window', 'U_floor'],'shgc','COP_ac','COP_hp','battery_cap'], [0.9, 1, 1.1])
#PlotBaseCase(CHE_HOUSES_SENSITIVITY).plt_sensitivity_analysis() -> for plotting extract results to excel

CHE_HOUSES_TEMP_SENSITIVITY = simulate_sensitivity_temperature_setpoint(CHE_HOUSE_TYPES, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, list(range(295,302,1)))
PlotBaseCase(CHE_HOUSES_TEMP_SENSITIVITY).plt_temp_sensitivity(list(range(295,302,1)))
"""
#------------ Perform calculations of sim object ------------------

#u_value_CHE = simulate_uvalue_scenario(CHE_NEW_SFH, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, CHE_UVALUE_SCENARIO)
pvprod = simulate_house(SWE_OLD_MFH, T_OUTSIDE_2019_PAR, IRRADIATION_2019_PAR)


#--------------- Scale Up -------------------------------------------
"""
countries_dict = {'DE':{'Simulation':DE_HOUSES_SIMULATION, 'MFH':26994800,'SFH':16361800},
                  'FR':{'Simulation':FR_HOUSES_SIMULATION, 'MFH':  24665600,'SFH':  12934400},
                  'IT':{'Simulation':IT_HOUSES_SIMULATION, 'MFH':  13520000,'SFH':  12480000},
                  'ESP':{'Simulation':ESP_HOUSES_SIMULATION, 'MFH':  17449600,'SFH':  9150400},
                  'SWE':{'Simulation':SWE_HOUSES_SIMULATION, 'MFH': 2508050,'SFH':  2641950},
                'BUL':{'Simulation':BUL_HOUSES_SIMULATION, 'MFH':  1879290,'SFH':  2110710}}

PlotBaseCase(countries_dict).plot_scale_up()
"""
# -------------- Initialize Plotting objects ------------------------


pvplot = PlotBaseCase(pvprod)
pvplot.plt_t_inside(168, SETPOINT_AC_CH, SETPOINT_HP_CH)


# ---------------------- Plot output --------------------------

avg_window = 168


"""
SWE_COMPARE_PLOT.plt_t_inside(avg_window, SETPOINT_AC_SWE, SETPOINT_HP_SWE)
SWE_COMPARE_PLOT.bar_ac_consumption()
SWE_COMPARE_PLOT.bar_hp_consumption()
SWE_COMPARE_PLOT.bar_net_demand()

BUL_COMPARE_PLOT.plt_t_inside(avg_window, SETPOINT_AC_BUL, SETPOINT_HP_BUL)
BUL_COMPARE_PLOT.bar_ac_consumption()
BUL_COMPARE_PLOT.bar_hp_consumption()
BUL_COMPARE_PLOT.bar_net_demand()

DE_COMPARE_PLOT.plt_t_inside(avg_window, SETPOINT_AC_DE, SETPOINT_HP_DE)
DE_COMPARE_PLOT.bar_ac_consumption()
DE_COMPARE_PLOT.bar_hp_consumption()
DE_COMPARE_PLOT.bar_net_demand()

FR_COMPARE_PLOT.plt_t_inside(avg_window, SETPOINT_AC_FR, SETPOINT_HP_FR)
FR_COMPARE_PLOT.bar_ac_consumption()
FR_COMPARE_PLOT.bar_hp_consumption()
FR_COMPARE_PLOT.bar_net_demand()

IT_COMPARE_PLOT.plt_t_inside(avg_window, SETPOINT_AC_IT, SETPOINT_HP_IT)
IT_COMPARE_PLOT.bar_ac_consumption()
IT_COMPARE_PLOT.bar_hp_consumption()
IT_COMPARE_PLOT.bar_net_demand()
"""

#print_stats(CHE_HOUSES_SIMULATION, 'SWITZERLAND')

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

