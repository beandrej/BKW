import numpy as np
import pandas as pd
from numpy import array
from solarpy import irradiance_on_plane, solar_panel
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

hours = np.arange(0, 8760, 1)

class solarRadiation:
    def __init__(self, height, lat):
        self.startDate = datetime(1999, 1, 1, 0)
        self.endDate = datetime(1999, 12, 31, 23)

        self.vnorm = np.array([0, 0, -1])
        self.height = height  
        self.lat = lat
        self.dateList = []
    
    def get_radiation(self):
        self.solarRadiationList = []
        currentDate = self.startDate
        while currentDate <= self.endDate:
            for hour in range(24):
                date = currentDate.replace(hour=hour)
                self.solarRadiationList.append(irradiance_on_plane(self.vnorm, self.height, date, self.lat))
            currentDate += timedelta(days=1)
        return (self.solarRadiationList)

class Panel:
    def __init__(self, surface, eff, orientation, lat,  alt):
        self.panel = solar_panel(surface, eff, id_name='Panel')
        self.panel.set_orientation(orientation)
        self.panel.set_position(lat, 5, alt)

        self.startDate = datetime(1999, 1, 1, 0)
        self.endDate = datetime(1999, 12, 31, 23)
        self.dateList = []

    def get_power(self):
        self.powerList = []
        currentDate = self.startDate
        while currentDate <= self.endDate:
            for hour in range(24):
                date = currentDate.replace(hour=hour, minute=0, second=0)
                self.panel.set_datetime(date)
                self.powerList.append(self.panel.power())
            currentDate += timedelta(days=1)
        return (self.powerList)

class PV:
    def __init__(self, path):
        self.PV_data = pd.read_csv(path)
        self.PV_output = list(self.PV_data.iloc[:, 1])

    def return_PV_list(self):
        print(self.PV_data.head())
        return self.PV_output

irr_2019_ZRH = solarRadiation(400, 44).get_radiation()

panel_orientation = array([0, 0, -1])
PV_generation_2019_ZRH = Panel(45, 0.2, panel_orientation, 44, 400).get_power()

PV_generation_2019_ZRH1 = PV("PV_data/PVoutput_2019.csv").return_PV_list()

print(len(PV_generation_2019_ZRH))
print(len(PV_generation_2019_ZRH1))
hours = np.arange(0, 8760, 1)

plt.plot(hours, PV_generation_2019_ZRH, label='solarpy')
plt.plot(hours, PV_generation_2019_ZRH1, label='solaR')
plt.legend()
plt.show()