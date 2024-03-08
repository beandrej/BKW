import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from House import House

# GLOBAL VARIABLES
hours_in_year = list(np.arange(0, 8761, 1))
days_in_year = [i/24 for i in hours_in_year]
t_initial = 293
t_des = 286
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
SFH_after_2000 = House(105, 17, 89, 0.2, 1.2, 0.3, 5, 3000, 0.6, 0.35, 3, 0.7)
SFH_before_2000 = House(105, 17, 89, 0.63, 2.7, 1.2, 5, 3000, 0.6, 0.35, 3, 1.4)

T_SFH_before = [t_initial]
T_SFH_after = [t_initial]

elec_demand_SFH_after = [0]
elec_demand_SFH_before = [0]

#CALCULATE
timestep = 1
for idx, t in enumerate(temp_list_kelvin):
    T_SFH_before_next = T_SFH_before[idx] + SFH_after_2000.get_t_diff(timestep, t, T_SFH_before[idx], irr_list[idx])
    T_SFH_after_next = T_SFH_after[idx] + SFH_after_2000.get_t_diff(timestep, t, T_SFH_after[idx], irr_list[idx])

    T_SFH_before.append(T_SFH_before_next)
    T_SFH_after.append(T_SFH_after_next)

    if T_SFH_before_next > t_des:
        elec_demand_SFH_before.append(SFH_before_2000.cooling_cap)
    else:
        elec_demand_SFH_before.append(0)

    if T_SFH_after_next > t_des:
        elec_demand_SFH_after.append(SFH_after_2000.cooling_cap)
    else:
        elec_demand_SFH_after.append(0)

print(f'Total cooling demand needed for SFH before 2000: {round(sum(elec_demand_SFH_before)/cop/1e6, 3)}[MW]')
print(f'Total cooling demand needed for SFH after 2000: {round(sum(elec_demand_SFH_after)/cop/1e6, 3)}[MW]')

# PLOT
plot_t_series = True
plot_demand = False

if plot_t_series:
    plt.plot(days_in_year, T_SFH_before, label='SFH after 2000')
    plt.plot(days_in_year, T_SFH_after, label='SFH before 2000')
    plt.axhline(y=t_des, color='r', linestyle='dotted', label='T_desired')
    plt.xlabel('Days in year')
    plt.ylabel('Temperature [K]')
    plt.title('Inside temperature of the house')
    plt.legend()
    plt.show()

if plot_demand:
    plt.plot(days_in_year, elec_demand_ac, label='Cooling demand over the year')
    plt.xlabel('Days in year')
    plt.ylabel('Cooling demand [W]')
    plt.title('Cooling demand over the year')
    plt.legend()
    plt.show()

print(SFH_after_2000.set_inertia())