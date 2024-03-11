import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from House import House, RunSimulation, Plot_output, PV

# GLOBAL VARIABLES
hours_in_year = list(np.arange(0, 8761, 1))
days_in_year = [i / 24 for i in hours_in_year]

# DATA IMPORT & FORMATING
T_2019_ZRH_file_path = r"ren_ninja/ZRH_2019_t2m.csv"
T_2019_ZRH_csv = pd.read_csv(T_2019_ZRH_file_path, delimiter=",", header=3)["t2m"].tolist()
T_outside_2019_ZRH = [temp + 273.15 for temp in T_2019_ZRH_csv]

irr_2019_ZRH_file_path = r"ren_ninja/ninja_weather_47.3744_8.5410_uncorrected.csv"
irr_2019_ZRH = pd.read_csv(irr_2019_ZRH_file_path, delimiter=",", header=3)["swgdn"].tolist()

PV_generation_2019_ZRH = PV("PV_data/PVoutput_2019.csv")

# PARAMETERS OF HOUSES
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
        "t_des": 293,
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
        "shgc": 0.6,
        "perc_s_windows": 0.35,
        "people": 3,
        "v_rate": 1.4,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 295,
        "t_des": 293,
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
        "heating_cap": 4000,
        "shgc": 0.6,
        "perc_s_windows": 0.3,
        "people": 10,
        "v_rate": 0.7,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 295,
        "t_des": 293,
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
        "shgc": 0.6,
        "perc_s_windows": 0.35,
        "people": 3,
        "v_rate": 0.7,
        "setpoint_ac": 295,
        "setpoint_hp": 293,
        "shade_factor": 0.7,
        "t_initial": 295,
        "t_des": 293,
        "wall_th": 0.1
    }
}

# INITIALIZING SIMULATION OBJECTS
simulations_CH_2019 = {}
scenario_output = {}
comparison = {}
comparison_output = {}

scenario_Switzerland = {
    "years": ["2020", "2030", "2040", "2050"],
    "temp_develop": [0, 0.5, 0.5, 0.5],
}

for house_name, params in house_params.items():
    house_obj = House(**params)
    simulations_CH_2019[house_name] = RunSimulation(house_obj, T_outside_2019_ZRH, irr_2019_ZRH, 3600, scenario_Switzerland)
    comparison[house_name] = RunSimulation(house_obj, T_outside_2019_ZRH, irr_2019_ZRH, 3600)

# CALCULATION
for house_type in comparison:
    comparison_output[house_type] = comparison[house_type].run()

scenario_output = simulations_CH_2019["modern_MFH"].run_scenario()
PV_generation_2019_ZRH = PV("PV_data/PVoutput_2019.csv")



# PLOT
plot2 = Plot_output(comparison_output, PV_generation_2019_ZRH.return_PV_list())
plot2.plot_temp_compare(100)

plots = Plot_output(scenario_output, PV_generation_2019_ZRH.return_PV_list())
plots.plot_temperature_scenario(24)
plots.plot_ac_demand()
plots.plot_aggregated_ac_demand_over_years()
plots.plot_base_case_with_PV()

# print(f'Total cooling demand needed for SFH before 2000: {round(tot_demand)} [W]')
