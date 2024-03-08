import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from House import House

hours_in_year = list(np.arange(0, 8761, 1))
days_in_year = [i/24 for i in hours_in_year]
t_des = House.t_des
cop = 3.5

# DATA IMPORT & FORMATING
T_file = r'ren_ninja/ZRH_2019_t2m.csv'
t_data = pd.read_csv(T_file, delimiter=',', header=3)
t_data = t_data['t2m']
temp_list = list(t_data)
temp_list_kelvin = [i + 273.15 for i in temp_list] # HIGHER TEMP 293.15, CUZ SOLAR TERM IGNORED IN House.py

S_file = r'ren_ninja/ninja_weather_47.3744_8.5410_uncorrected.csv'
s_data = pd.read_csv(S_file, delimiter=',', header=3)
s_data = s_data['swgdn']
irr_list = list(s_data)


# INITIALIZE OBJECT
old_house = House(200, 20, 80, 2, 4.8, 1, 2.5, 0, 0.75, 2, 4)
old_house_with_ac = House(200, 20, 80, 2, 4.8, 1, 2.5, 5000, 0.75, 2, 4)

t_series_old = [old_house.t_initial]
t_series_old_ac = [old_house_with_ac.t_initial]

elec_demand_ac = [0]

#CALCULATE 
timestep = 1
for idx, t in enumerate(temp_list_kelvin):
    t_next_old = t_series_old[idx] + old_house.get_t_diff(timestep, t, t_series_old[idx], irr_list[idx])
    t_next_old_ac = t_series_old_ac[idx] + old_house_with_ac.get_t_diff(timestep, t, t_series_old_ac[idx], irr_list[idx])

    t_series_old.append(t_next_old)
    t_series_old_ac.append(t_next_old_ac)

    if t_next_old_ac > t_des:
        elec_demand_ac.append(old_house_with_ac.cooling_cap)
    else:
        elec_demand_ac.append(0)

print(f'Total cooling demand needed: {round(sum(elec_demand_ac)/cop/1e6, 3)}[MW]')

# PLOT
plot_t_series = False
plot_demand = True

if plot_t_series:
    plt.plot(days_in_year, t_series_old, label='No AC')
    plt.plot(days_in_year, t_series_old_ac, label='With AC')
    
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