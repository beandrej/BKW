import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from House import House, RunSimulation, ACUnit, Plot_output, PV

# GLOBAL VARIABLES
hours_in_year = list(np.arange(0, 8761, 1))
days_in_year = [i/24 for i in hours_in_year]
#t_initial = 295
#t_des = 295
delta_t_des = 1
cop = 3.5



# DATA IMPORT & FORMATING
T_file = r'ren_ninja/ZRH_2019_t2m.csv'
t_data = pd.read_csv(T_file, delimiter=',', header=3)
t_data = t_data['t2m']
temp_list = list(t_data)
temp_list_kelvin = [i + 273.15 for i in temp_list]

S_file = r'ren_ninja/ninja_weather_47.3744_8.5410_uncorrected.csv'
s_data = pd.read_csv(S_file, delimiter=',', header=3)
s_data = s_data['swgdn']
irr_list = list(s_data)

# PARAMETERS OF HOUSES
scenario_SFH_after_2000 = {"U_window": 1.2 , "U_wall": 0.2 ,"U_floor": 0.3, "A_window": 17 ,"A_wall":105, "A_floor":89, "shgc":0.6, "v_rate":0.7, "perc_s_window": 0.35 }
scenario_SFH_before_2000 = {"U_window": 2.7, "U_wall":0.63,"U_floor":1.2, "A_window": 17,"A_wall":105, "A_floor":89, "shgc":0.6, "v_rate":1.4, "perc_s_window": 0.35}
scenario_MFH_after_2000 = {"U_window": 1.3 , "U_wall": 0.2 ,"U_floor": 0.3, "A_window": 80, "A_wall":279,"A_floor":252, "shgc":0.6, "v_rate":0.7, "perc_s_window": 0.3}
scenario_MFH_before_2000 = {"U_window": 2.8, "U_wall":0.8,"U_floor":1.3,"A_wall":279,"A_window": 80 ,"A_floor":252,"shgc":0.6, "v_rate":1.4, "perc_s_window": 0.3 }

# INITIALIZE OBJECT
SFH_after_2000 = House(105, 17, 89, 0.2, 1.2, 0.3, 5, 4000,4000, 0.6, 0.35,3 ,0.7, 295, 293)
MFH_before_2000 = House(279, 80, 252, 0.8, 2.8, 1.3, 5, 4000,4000, 0.6, 0.35,3 ,0.7, 295, 293)
#SFH_before_2000 = House(105, 17, 89, 0.63, 2.7, 1.2, 5, 3000, 0.6, 0.35, 3, 1.4)
scenario_Switzerland = {"years":["2020","2030","2040","2050"], "temp_develop":[0,0.5,0.5,0.5]}
# SIMULATION
#test_obj = RunSimulation(SFH_after_2000, temp_list_kelvin, irr_list, 3600)
#test_obj = RunSimulation(MFH_before_2000, temp_list_kelvin, irr_list, 3600)
#sfh_t_list, sfh_e_demand, tot_demand = test_obj.run()

#Running scenarios
test_obj = RunSimulation(SFH_after_2000, temp_list_kelvin, irr_list, 3600, scenario_Switzerland)
scenario_output=test_obj.run_scenario()
PV_generation = PV("PV_data/PVoutput_2019.csv")
plots=Plot_output(scenario_output,PV_generation.return_PV_list())
plots.plot_temperature()
plots.plot_ac_demand()
plots.plot_aggregated_ac_demand_over_years()
plots.plot_base_case_with_PV()

#print(f'Total cooling demand needed for SFH before 2000: {round(tot_demand)} [W]')

# PLOT
plot_t_series = False
plot_demand = False

if plot_t_series:
    plt.plot(days_in_year, sfh_t_list, label='SFH after 2000')
    #plt.plot(days_in_year, T_SFH_before, label='SFH before 2000')
    plt.axhline(y=t_des, color='r', linestyle='dotted', label='T_desired')
    plt.xlabel('Days in year')
    plt.ylabel('Temperature [K]')
    plt.title('Inside temperature of the house')
    plt.legend()
    plt.show()

if plot_demand:
    plt.plot(days_in_year, sfh_e_demand, label='Cooling demand over the year')
    plt.xlabel('Days in year')
    plt.ylabel('Cooling demand [W]')
    plt.title('Cooling demand over the year')
    plt.legend()
    plt.show()

#print(SFH_after_2000.set_inertia())