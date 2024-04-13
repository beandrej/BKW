import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from House import House, RunSimulation, Plot_output, PV
from parameters import SETPOINT_AC, SETPOINT_HP

# ------------------ Data import -----------------

T_2019_ZRH_file_path = r"ren_ninja/ZRH_2019_t2m.csv"
irr_2019_ZRH_file_path = r"ren_ninja/ninja_weather_47.3744_8.5410_uncorrected.csv"
T_2019_ZRH_csv = pd.read_csv(T_2019_ZRH_file_path, delimiter=",", header=3)["t2m"].tolist()

T_OUTSIDE_2019_ZRH = [temp + 273.15 for temp in T_2019_ZRH_csv] # convert to kelvin
IRRADIATION_2019_ZRH = pd.read_csv(irr_2019_ZRH_file_path, delimiter=",", header=3)["swgdn"].tolist()
PV_GEN_2019_ZRH = PV("PV_data/PVoutput_2019.csv")

# ------------- Define parameters of house types -----------

from parameters import CH_HOUSE_TYPES, BATTERY_COMPARSION

#-------------- Initialize simulation objects -----------------

simulations_CH_2019 = {}
scenario_output = {}
CH_HOUSE_SIMULATION = {}
BATTERY_COMPARISON_SIMULATION = {}
comparison_battery_output = {}
comparison_output = {}

scenario_Switzerland = {
    "years": ["2020", "2030", "2040", "2050"],
    "temp_develop": [0, 0.5, 0.5, 0.5],
}

#-------------- Read house params and initialize sim object with << RunSimulation >> ------------

for house_name, params in CH_HOUSE_TYPES.items():
    obj = House(**params)
    simulations_CH_2019[house_name] = RunSimulation(obj, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, 3600, scenario_Switzerland)
    CH_HOUSE_SIMULATION[house_name] = RunSimulation(obj, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, 3600)

for house, param in BATTERY_COMPARSION.items():
    house_obj_battery = House(**param)
    BATTERY_COMPARISON_SIMULATION[house] = RunSimulation(house_obj_battery, T_OUTSIDE_2019_ZRH, IRRADIATION_2019_ZRH, 3600)

#------------ Perform calculations of sim object ------------------

for house_type in CH_HOUSE_SIMULATION:
    comparison_output[house_type] = CH_HOUSE_SIMULATION[house_type].run()

# for house_type1 in comparison_battery:
#     comparison_battery_output[house_type1] = comparison_battery[house_type1].run()


#scenario_output = simulations_CH_2019["modern_MFH"].run_scenario()


#------------ Plot resulting output ----------------



#plot2battery = Plot_output(comparison_battery_output, PV_generation_2019_ZRH.return_PV_list())

plot2 = Plot_output(comparison_output, PV_GEN_2019_ZRH)
plot2.plt_net_demand()
plot2.plt_SOC_battery(168)
plot2.plt_ac_consumption()
plot2.plt_t_inside(169, SETPOINT_AC, SETPOINT_HP)
plot2.bar_plot_battery_comparison()

# plots = Plot_output(scenario_output, PV_GEN_2019_ZRH)
# plots.plot_temperature_scenario(168)
# plots.plot_ac_demand()
# plots.plot_aggregated_ac_demand_over_years()
# plots.plot_base_case_with_PV()

print(f'Cooling needed for old MFH: {round(sum((comparison_output['old_MFH'][1])) / (3.5 * 1e3), 2)} [MWh]')
print(f'Heating needed for old MFH: {round(sum(comparison_output['old_MFH'][5]) / (3.5 * 1e3), 2)} [MWh] \n')

print(f'Cooling needed for old SFH: {round(sum((comparison_output['old_SFH'][1])) / (3.5 * 1e3), 2)} [MWh]')
print(f'Heating needed for old SFH: {round(sum(comparison_output['old_SFH'][5]) / (3.5 * 1e3), 2)} [MWh] \n')

# print(f'Total electricity with Battery for old SFH: {round(comparison_output['old_SFH'][6]) / 1e6} [MW]')
# print(f'Cooling needed for old SFH: {round(comparison_output['old_SFH'][2]) / 1e6} [MW]')

# print(f'Total electricity with Battery for modern MFH: {round(comparison_output['modern_MFH'][6]) / 1e6} [MW]')
# print(f'Cooling needed for modern MFH: {round(comparison_output['modern_MFH'][2]) / 1e6} [MW]')

# print(f'Total electricity with Battery for modern SFH: {round(comparison_output['modern_SFH'][6]) / 1e6} [MW]')
# print(f'Cooling needed for modern SFH: {round(comparison_output['modern_SFH'][2]) / 1e6} [MW]')



