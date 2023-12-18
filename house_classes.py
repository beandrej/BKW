import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

air_density = 1.293 #[kg/m^3]
cp_air = 1005*air_density #[J/(m^3*K)]
hours_in_year = list(np.arange(1,8762,1))
days_in_year = [i/24 for i in hours_in_year]
cop = 3.5

class House:

    t_initial = 300
    t_des = 300
    delta_t_des = 1
    
    
    def __init__(self, A_wall, A_window, A_floor, U_wall, U_window, U_floor, height, cooling_cap):
        self.A_wall = A_wall #[m^2]
        self.A_window = A_window #[m^2]
        self.A_floor = A_floor #[m^2]
        self.U_wall = U_wall #[W/(m^2*K)]
        self.U_window = U_window #[W/(m^2*K)]
        self.U_floor = U_floor #[W/(m^2*K)]
        self.height = height #[m]
        self.cooling_cap = cooling_cap #[W]
        self.ac = self.initialize_ac()
        self.inertia = self.initialize_inertia()

    def initialize_ac(self):
        self.ac = 0
        if self.t_initial < self.t_des - self.delta_t_des:
            self.ac = 0
            return self.ac
        elif self.t_initial > self.t_des + self.delta_t_des:
            self.ac
            return self.ac
        else:
            return self.ac
    
    def initialize_inertia(self): #[J/K]
        return cp_air * self.A_floor * self.height

    def get_heat_gain_from_env(self, t_out, t_in): # [J], heat gain per timestep
        heat_gain = (self.A_wall * self.U_wall + self.A_window * self.U_window + self.A_floor * self.U_floor) * (t_out - t_in)
        #solar_term = 0
        return heat_gain   

    def ac_on(self, t_in): #[0 or 1]
        
        if t_in < self.t_des - self.delta_t_des:
            self.ac = 0
            return self.ac
        
        elif t_in > self.t_des + self.delta_t_des:
            self.ac = 1
            return self.ac
        else:
            return self.ac


    def get_temp_diff(self, timestep, t_out, t_in): #[K]
        t_diff = (self.get_heat_gain_from_env(t_out, t_in)*timestep / self.inertia) 
        + (self.ac_on(t_in)*self.cooling_cap*timestep / self.inertia)
        return t_diff 

# DATA IMPORT & FORMATING
file_name = r'ch_temp_2019/temp_data_2019.csv'
t_data = pd.read_csv(file_name, delimiter=',', header=3)
t_data = t_data['t2m']
temp_list = list(t_data)
temp_list_kelvin = [i + 283.15 for i in temp_list]



old_house = House(200, 20, 80, 2, 4.8, 1, 2.5, 5000000)
med_house = House(200, 20, 80, 1, 2, 1, 2.5, 5000)
new_house = House(200, 20, 80, 0.5, 1.2, 1, 2.5, 5000)

t_series_old = []
t_series_med = []
t_series_new = []

t_series_old.append(old_house.t_initial)
t_series_med.append(med_house.t_initial)
t_series_new.append(new_house.t_initial)

timestep = 100 #[s], should be set to 3600 cuz data is hourly but then it crashes^^

for idx, t in enumerate(temp_list_kelvin):
    t_next_old = t_series_old[idx] + old_house.get_temp_diff(timestep, t, t_series_old[idx])
    t_next_med = t_series_med[idx] + med_house.get_temp_diff(timestep, t, t_series_med[idx])
    t_next_new = t_series_new[idx] + new_house.get_temp_diff(timestep, t, t_series_new[idx])
    
    t_series_old.append(t_next_old)
    t_series_med.append(t_next_med)
    t_series_new.append(t_next_new)
    print(old_house.ac_on(t_next_old))
    #print(t_next_old)


plt.plot(days_in_year, t_series_old)
plt.plot(days_in_year, t_series_med)
plt.plot(days_in_year, t_series_new)

plt.xlabel('Hours in year')
plt.ylabel('Temperature [K]')
plt.title('Inside temperature of the house')


plt.show()