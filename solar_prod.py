import numpy as np
import matplotlib.pyplot as plt

def rad(deg):
    return deg*np.pi/180

panel_inclination = rad(46)
panel_orientation = rad(0)

solar_irr = 1000
efficiency = 0.25

longitude = rad(5)
latitude = rad(44)

day_of_year = np.arange(1, 366, 1).tolist()
hours_of_day = np.arange(1, 25, 1).tolist()
hours_of_year = hours_of_day * 365
time = np.arange(1, 8761, 1).tolist()


declination = [rad(23.45) * np.sin (rad(360)*(284+day)/365) for day in day_of_year]
delta_s = [x for x in declination for _ in range(len(hours_of_day))]
omega = [rad(15)*(hour - 12) for hour in hours_of_day]
omega_for_year = omega * 365
alpha_s = [np.arcsin(np.sin(latitude) * np.sin(decl) + np.cos(latitude) * np.cos(hour) * np.cos(decl)) for hour in omega for decl in declination]
theta_z = [np.arccos(np.sin(i)) for i in alpha_s]
gamma_s = [np.arcsin((np.cos(x) * np.sin(y) / np.cos(z))/(2*np.pi)) for x, y, z in zip(delta_s, omega_for_year, alpha_s)]
theta = [np.arccos(np.cos(t_z) * np.cos(panel_inclination) + np.sin(t_z) * np.sin(panel_inclination) * np.cos(g_s - panel_orientation)) for t_z, g_s in zip(theta_z, gamma_s)]

sunrise = [12 - (np.arccos(-np.tan(latitude) * np.tan(i)) / rad(15)) for i in delta_s]
sunset = [12 + (np.arccos(-np.tan(latitude) * np.tan(i)) / rad(15)) for i in delta_s]

r_t = [x / y for x, y in zip(theta, theta_z)]

irr_raw = [1000*np.cos(x) if sunrise_hour < hour < sunset_hour else 0 for x, hour, sunrise_hour, sunset_hour in zip(theta, hours_of_year, sunrise, sunset) ]
irr = [x if x >= 0 else 0 for x in irr_raw]

energy = [x * efficiency for x in irr]


plt.plot(time, irr)
plt.plot(time, energy)

plt.show()