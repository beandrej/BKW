import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from House import House, RunSimulation, Plot_output, PV

# ------------------ Global variables -----------

hours_in_year = list(np.arange(0, 8761, 1))
days_in_year = [i / 24 for i in hours_in_year]

# ------------------ Data import -----------------

T_2019_ZRH_file_path = r"ren_ninja/ZRH_2019_t2m.csv"
T_2019_ZRH_csv = pd.read_csv(T_2019_ZRH_file_path, delimiter=",", header=3)["t2m"].tolist()
T_outside_2019_ZRH = [temp + 273.15 for temp in T_2019_ZRH_csv] # convert to kelvin

irr_2019_ZRH_file_path = r"ren_ninja/ninja_weather_47.3744_8.5410_uncorrected.csv"
irr_2019_ZRH = pd.read_csv(irr_2019_ZRH_file_path, delimiter=",", header=3)["swgdn"].tolist()

PV_generation_2019_ZRH = PV("PV_data/PVoutput_2019.csv")

# ------------- Define parameters of house types -----------

house_params = {
    "modern_SFH": {
        "A_wall": 105,
        "A_window": 17,
        "A_floor": 89,
        "U_wall": 0.2,
        "U_window": 1.2,
        "U_floor": 0.3,
        "height": 5,
        "cooling_cap": 4000,
        "heating_cap": 4000,
        "shgc": 0.6,
        "perc_s_windows": 0.35,
        "people": 3,
        "v_rate": 0.7,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 295,
        "wall_th": 0.1
    },
    "old_SFH": {
        "A_wall": 105,
        "A_window": 17,
        "A_floor": 89,
        "U_wall": 0.63,
        "U_window": 2.7,
        "U_floor": 1.2,
        "height": 5,
        "cooling_cap": 4000,
        "heating_cap": 4000,
        "shgc": 0.2,
        "perc_s_windows": 0.35,
        "people": 3,
        "v_rate": 1.4,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 295,
        "wall_th": 0.1
    },
    "modern_MFH": {
        "A_wall": 279,
        "A_window": 80,
        "A_floor": 252,
        "U_wall": 0.2,
        "U_window": 1.3,
        "U_floor": 0.3,
        "height": 10,
        "cooling_cap": 4000,
        "heating_cap": 8000,
        "shgc": 0.2,
        "perc_s_windows": 0.3,
        "people": 10,
        "v_rate": 0.7,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 295,
        "wall_th": 0.1
    },
    "old_MFH": {
        "A_wall": 279,
        "A_window": 80,
        "A_floor": 252,
        "U_wall": 0.8,
        "U_window": 2.8,
        "U_floor": 1.3,
        "height": 10,
        "cooling_cap": 4000,
        "heating_cap": 4000,
        "shgc": 0.2,
        "perc_s_windows": 0.35,
        "people": 10,
        "v_rate": 0.7,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 280,
        "wall_th": 0.1
    }
}

#-------------- Initialize simulation objects -----------------

simulations_CH_2019 = {}
scenario_output = {}
comparison = {}
comparison_output = {}
total_demand_ac = 0

scenario_Switzerland = {
    "years": ["2020", "2030", "2040", "2050"],
    "temp_develop": [0, 0.5, 0.5, 0.5],
}

#-------------- Read house params and initialize sim object with << RunSimulation >> ------------

for house_name, params in house_params.items():
    house_obj = House(**params)
    simulations_CH_2019[house_name] = RunSimulation(house_obj, T_outside_2019_ZRH, irr_2019_ZRH, 3600, scenario_Switzerland)
    comparison[house_name] = RunSimulation(house_obj, T_outside_2019_ZRH, irr_2019_ZRH, 3600)


#------------ Perform calculations of sim object ------------------
    
for house_type in comparison:
    comparison_output[house_type] = comparison[house_type].run()

scenario_output = simulations_CH_2019["modern_MFH"].run_scenario()


#------------ Plot resulting output ----------------

plot2 = Plot_output(comparison_output, PV_generation_2019_ZRH.return_PV_list())
plot2.plot_temp_compare(168)

plots = Plot_output(scenario_output, PV_generation_2019_ZRH.return_PV_list())
plots.plot_temperature_scenario(168)
plots.plot_ac_demand()
plots.plot_aggregated_ac_demand_over_years()
#plots.plot_base_case_with_PV()


print(f'Total electricity needed for old MFH: {round(comparison_output['old_MFH'][4]) / 1e6} [MW]')
print(f'Cooling needed for old MFH: {round(comparison_output['old_MFH'][2]) / 1e6} [MW]')
print(f'Heating needed for old MFH: {round(comparison_output['old_MFH'][3]) / 1e6} [MW]\n')

print(f'Total electricity needed for old SFH: {round(comparison_output['old_SFH'][4]) / 1e6} [MW]')
print(f'Cooling needed for old SFH: {round(comparison_output['old_SFH'][2]) / 1e6} [MW]')
print(f'Heating needed for old SFH: {round(comparison_output['old_SFH'][3]) / 1e6} [MW]\n')

print(f'Total electricity needed for modern MFH: {round(comparison_output['modern_MFH'][4]) / 1e6} [MW]')
print(f'Cooling needed for modern MFH: {round(comparison_output['modern_MFH'][2]) / 1e6} [MW]')
print(f'Heating needed for modern MFH: {round(comparison_output['modern_MFH'][3]) / 1e6} [MW]\n')

print(f'Total electricity needed for modern SFH: {round(comparison_output['modern_SFH'][4]) / 1e6} [MW]')
print(f'Cooling needed for modern SFH: {round(comparison_output['modern_SFH'][2]) / 1e6} [MW]')
print(f'Heating needed for modern SFH: {round(comparison_output['modern_SFH'][3]) / 1e6} [MW]\n')
