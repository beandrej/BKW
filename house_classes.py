import pandas as pd
import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np


class House:

    t_des = 302
    delta_t_des = 1

    def __init__(self, A_wall, A_window, A_floor, U_wall, U_window, U_floor, height, cooling_cap):
        self.A_wall = A_wall
        self.A_window = A_window
        self.A_floor = A_floor
        self.U_wall = U_wall
        self.U_window = U_window
        self.U_floor = U_floor
        self.height = height
        self.cooling_cap = cooling_cap

    def get_delta_c(self):
        return cp_air * self.A_floor * self.height

    def get_heat_gain(self, t_out, t_in):
        temp_term = (self.A_wall * self.U_wall + self.A_window * self.U_window + self.A_floor * self.U_floor) * (t_out - t_in)
        solar_term = 0
        return (temp_term + solar_term)/3600
    

    def get_w_ac(self, t_in):
        
        if t_in < self.t_des - self.delta_t_des:
            w_ac = 0
            return w_ac
        
        elif t_in > self.t_des + self.delta_t_des:
            w_ac = 1
            return w_ac
        
        else:
            w_ac = 0
            return w_ac


    def get_temp_diff(self, delta_t, t_out, t_in):
        t_add = delta_t/3600 * self.get_heat_gain(t_out, t_in) / self.get_delta_c() + delta_t/3600 * self.cooling_cap * self.get_w_ac(t_in) / self.get_delta_c() 
        return t_add

cp_air = 4.18
cop = 3.5
t_initial = 250


file_name = r'ch_temp_2019/temp_data_2019.csv'
t_data = pd.read_csv(file_name, delimiter=',', header=3)
t_data = t_data['t2m']
temp_list = list(t_data)
temp_list_kelvin = [i + 273.15 for i in temp_list]

old_house = House(200, 20, 80, 2, 4.8, 1, 2.5, 5000)
med_house = House(200, 20, 80, 1, 2, 1, 2.5, 5000)
new_house = House(200, 20, 80, 0.5, 1.2, 1, 2.5, 5000)

t_series_old = []
t_series_med = []
t_series_new = []

t_series_old.append(t_initial)
t_series_med.append(t_initial)
t_series_new.append(t_initial)


for idx, t in enumerate(temp_list_kelvin):
    t_next_old = t_series_old[idx] + old_house.get_temp_diff(3600, t, t_series_old[idx])
    t_next_med = t_series_med[idx] + med_house.get_temp_diff(3600, t, t_series_med[idx])
    t_next_new = t_series_new[idx] + new_house.get_temp_diff(3600, t, t_series_new[idx])

    t_series_old.append(t_next_old)
    t_series_med.append(t_next_med)
    t_series_new.append(t_next_new)




hours_in_year = np.arange(1,8762,1)

plt.plot(hours_in_year, t_series_old)
plt.plot(hours_in_year, t_series_med)
plt.plot(hours_in_year, t_series_new)

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('X on Y Plot')


plt.show()