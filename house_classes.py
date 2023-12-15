import pandas as pd
import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np

class House:

    T_in = 300
    solar_irr = 1000
    pr = 0.75

    def __init__(self, area, wall_area, insulation, persons, panel):
        self.area = area #surface area
        self.wall_area = wall_area #surface area of walls
        self.insulation = insulation #insulation value
        self.persons = persons #number of persons in the house
        self.panel = panel

    def cooling_demand(self, T_out):
        Q = self.wall_area*self.insulation*(T_out - House.T_in)*0.024 + self.persons*3
        return Q
    
    def solar_prod(self, efficiency):
        E = self.panel*efficiency*House.solar_irr*House.pr
        return E        




plot_it = 1

houseCH = House(200, 400, 0.15, 3, 1)

file_name = r'weather_data.csv'
t_data = pd.read_csv(file_name, delimiter=',')
t_data.fillna(0, inplace=True)

print(t_data)
dataCH = t_data[['utc_timestamp', 'CH_temperature']]

q_houseCH = []
timestamp = np.arange(len(dataCH))/8650 + 1980
print(timestamp)

for T in dataCH['CH_temperature']:
    q_houseCH.append(houseCH.cooling_demand(T))

if plot_it == True:
    plt.plot(timestamp, q_houseCH, label='CH')
    plt.legend()
    plt.show()

































































# temp_data_file_name = r'data_sample.csv'
# temp_data = pd.read_csv(temp_data_file_name, delimiter=',')
# temp_data.dropna(inplace=True)
# data = temp_data.iloc[:, 3000]

# file_path = r'p95_Tmax_Yearly_rcp85_mean_v1.0.nc'
# nc_file = nc.Dataset(file_path, 'r')

# print(nc_file.variables.keys())

# # Access the 'lat' and 'lon' variables
# lat_variable = nc_file.variables['lat'][:]
# lon_variable = nc_file.variables['lon'][:]

# # Define the target latitude and longitude values
# target_lat = 44
# target_lon = 3

# # Find the indices where 'lat' and 'lon' match the target values
# lat_indices = (lat_variable == target_lat)
# lon_indices = (lon_variable == target_lon)
# print(nc_file.variables.keys())
# variable_names = nc_file.variables.keys()
# desired_data = nc_file.variables['p95_Tmax_Yearly'][:, lat_indices, lon_indices]
# print(desired_data)

# temp_nc = []

