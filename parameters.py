

""" __________________________________________"""

""" --------- SET HOUSE PARAMETERS ---------- """

"""___________________________________________"""



# ---------- SAME FOR ALL HOUSES -------------

WALL_THICKNESS = 0.3 # Wall thickness [m]
VENTILATON_RATE = 0.7 # Ventilation rate [1/h] (little impact)
T_INITIAL = 295 # Initial Temperature inside the house [K]

WINDOWS_SHADE_FACTOR = 0.5 # Shading factor of windows [0 to 1]
WINDOWS_FACING_SOUTH = 0.35 # Percentage of windows facing south [0 to 1]

# ---------------- AC / HP / BATTERY ---------------------

AC_CAPACITY_SFH = 4000 # Air conditioner capacity for Single family house (SFH) [W]
AC_CAPACITY_MFH = 6000 # Air conditioner capacity for Multi family house (MFH) [W]

HP_CAPACITY_SFH = 6000 # Heat pump capacity for Single family house (SFH) [W]
HP_CAPACITY_MFH = 9000 # Heat pump capacity for Multi family house (MFH) [W]

AC_COP = 3.5
HP_COP = 3.5

BATTERY_STORAGE_SFH = 0 # Battery storage for Single family house (SFH) [Wh]
BATTERY_STORAGE_MFH = 0 # Battery storage for Multi family house (MFH) [Wh]

BATTERY_THROUGHPUT_SFH = 0 # Battery throughput for Single family house (SFH) [W]
BATTERY_THROUGHPUT_MFH = 0 # Battery throughput for Multi family house (MFH) [W]

# ------------------- FIXED FOR SFH/MFH ----------------------

HEIGHT_SFH = 5 # Height of Single family house [m]
HEIGHT_MFH = 10 # Height of multi family house [m] 

PEOPLE_SFH = 3 # Number of people in single family house [#]
PEOPLE_MFH = 10 # Number of people in multi family house [#]

AREA_WALL_SFH = 105 # Area of walls in single family house [m2]
AREA_WALL_MFH = 279 # Area of walls in multi family house [m2]

AREA_WINDOW_SFH = 17 # Area of windows in single family house [m2]
AREA_WINDOW_MFH = 80 # Area of windows in multi family house [m2]

AREA_FLOOR_SFH = 89 # Area of floor in single family house [m2]
AREA_FLOOR_MFH = 252 # Area of floor in multi family house [m2]

# ------------------- SOLAR HEAT GAIN COEFFICIENT OF WINDOWS ---------------

SINGLE_GLAZED = 0.7 # Solar heat gain coefficient for single glazed windows [0 to 1]
DOUBLE_GLAZED = 0.45 # Solar heat gain coefficient for double glazed windows [0 to 1]
TRIPLE_GLAZED = 0.2 # Solar heat gain coefficient fo triple glazed windows [0 to 1]


"""_____________________________________________________________________"""

""" -------------------- COUNTRY SPECIFIC VALUES ---------------------- """

"""_____________________________________________________________________"""


# -------------------------- SWITZERLAND ----------------------------

U_WALL_NEW_CH = 0.2 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_CH = 0.63 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_CH = 1.2 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_CH = 2.7 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_CH = 0.3 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_CH = 1.2 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_CH = 273 + 25
SETPOINT_HP_CH = 273 + 17

# --------------------------- SPAIN --------------------------------

U_WALL_NEW_ESP = 2.04 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_ESP = 2.81 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_ESP = 8.24 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_ESP = 8.89 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_ESP = 1.39 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_ESP = 1.96 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_ESP = 273 + 27
SETPOINT_HP_ESP = 273 + 17

# --------------------------- SWEDEN -------------------------------

U_WALL_NEW_SWE = 0.85 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_SWE = 0.99 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_SWE = 3.84 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_SWE = 4.07 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_SWE = 0.78 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_SWE = 0.79 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_SWE = 273 + 25
SETPOINT_HP_SWE = 273 + 17

# -------------------------- BULGARIA -----------------------------

U_WALL_NEW_BUL = 0.75 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_BUL = 1.65 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_BUL = 3.85 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_BUL = 4.33 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_BUL = 0.45 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_BUL = 1.39 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_BUL = 273 + 25
SETPOINT_HP_BUL = 273 + 17

#------------------------------ Italy -------------------------------

U_WALL_NEW_IT_MFH = 0.28 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_IT_MFH = 0.97 # Wall thermal resistance [W/(m2*K)]
U_WALL_NEW_IT_SFH = 0.51 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_IT_SFH = 0.97 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_IT_MFH = 1.83 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_IT_MFH = 3.23 # Window thermal resistance [W/(m2*K)]
U_WINDOW_NEW_IT_SFH = 2.38 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_IT_SFH = 3.08 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_IT_MFH = 0.3 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_IT_MFH = 0.99 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_NEW_IT_SFH = 0.5 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_IT_SFH = 0.95 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_IT = 273 + 27
SETPOINT_HP_IT = 273 + 17

#-------------------------------- France -------------------------------
U_WALL_NEW_FR_MFH = 0.24 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_FR_MFH = 0.72 # Wall thermal resistance [W/(m2*K)]
U_WALL_NEW_FR_SFH = 0.22 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_FR_SFH = 0.76 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_FR_MFH = 1.13 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_FR_MFH = 2.68 # Window thermal resistance [W/(m2*K)]
U_WINDOW_NEW_FR_SFH = 1.13 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_FR_SFH = 2.86 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_FR_MFH = 0.23 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_FR_MFH = 0.78 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_NEW_FR_SFH = 0.2 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_FR_SFH = 0.65 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_FR = 273 + 25
SETPOINT_HP_FR = 273 + 17

#------------------------------Germany---------------------------
U_WALL_NEW_DE_MFH = 0.25 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_DE_MFH = 0.91 # Wall thermal resistance [W/(m2*K)]
U_WALL_NEW_DE_SFH = 0.29 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_DE_SFH = 0.74 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_DE_MFH = 1.38 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_DE_MFH = 2.44 # Window thermal resistance [W/(m2*K)]
U_WINDOW_NEW_DE_SFH = 1.45 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_DE_SFH = 2.7 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_DE_MFH = 0.35 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_DE_MFH = 0.62 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_NEW_DE_SFH = 0.37 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_DE_SFH = 0.66 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_DE = 273 + 25
SETPOINT_HP_DE = 273 + 17


"""___________________________________________"""

""" --------------- READ PV ------------------"""

"""___________________________________________"""


from House import read_PV

PV_2019_AT = read_PV("PV_data/Hourly_electricity_per_area_AT.csv")
PV_2019_BU = read_PV("PV_data/Hourly_electricity_per_area_BU.csv")
PV_2019_CH = read_PV("PV_data/Hourly_electricity_per_area_CH.csv")
PV_2019_DE = read_PV("PV_data/Hourly_electricity_per_area_DE.csv")
PV_2019_ES = read_PV("PV_data/Hourly_electricity_per_area_ES.csv")
PV_2019_FR = read_PV("PV_data/Hourly_electricity_per_area_FR.csv")
PV_2019_IT = read_PV("PV_data/Hourly_electricity_per_area_IT.csv")
PV_2019_SW = read_PV("PV_data/Hourly_electricity_per_area_SW.csv")

AREA_COVERED_BY_PV_SFH = 30
AREA_COVERED_BY_PV_MFH = 90

# ------------------------------------------------------------------

CHE_OLD_MFH = {
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_CH,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

ESP_OLD_MFH = {
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_ESP,
        "U_window": U_WINDOW_OLD_ESP,
        "U_floor": U_FLOOR_OLD_ESP,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_ESP,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_ESP,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_ES,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

SWE_OLD_MFH = {
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_SWE,
        "U_window": U_WINDOW_OLD_SWE,
        "U_floor": U_FLOOR_OLD_SWE,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_SWE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_SWE,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_SW,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

BUL_OLD_MFH = {
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_BUL,
        "U_window": U_WINDOW_OLD_BUL,
        "U_floor": U_FLOOR_OLD_BUL,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_BUL,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_BUL,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_BU,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

CHE_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_CH,
        "U_window": U_WINDOW_NEW_CH,
        "U_floor": U_FLOOR_NEW_CH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_CH,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_CH,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_CH,
        "U_window": U_WINDOW_NEW_CH,
        "U_floor": U_FLOOR_NEW_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_CH,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_CH,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

testest123 = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_CH,
        "U_window": U_WINDOW_NEW_CH,
        "U_floor": U_FLOOR_NEW_CH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_CH,
        "U_window": U_WINDOW_NEW_CH,
        "U_floor": U_FLOOR_NEW_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
        "SFH after n 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_CH,
        "U_window": U_WINDOW_NEW_CH,
        "U_floor": U_FLOOR_NEW_CH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
    "SFH before n 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
    "MFH after n 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_CH,
        "U_window": U_WINDOW_NEW_CH,
        "U_floor": U_FLOOR_NEW_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    },
    "MFH before n 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_CH,
        "U_window": U_WINDOW_OLD_CH,
        "U_floor": U_FLOOR_OLD_CH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_CH,
        "setpoint_hp": SETPOINT_HP_CH,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    }
}


ESP_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_ESP,
        "U_window": U_WINDOW_NEW_ESP,
        "U_floor": U_FLOOR_NEW_ESP,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_ESP,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_ESP,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_ES,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_ESP,
        "U_window": U_WINDOW_OLD_ESP,
        "U_floor": U_FLOOR_OLD_ESP,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_ESP,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_ESP,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_ES,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_ESP,
        "U_window": U_WINDOW_NEW_ESP,
        "U_floor": U_FLOOR_NEW_ESP,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_ESP,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_ESP,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_ES,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_ESP,
        "U_window": U_WINDOW_OLD_ESP,
        "U_floor": U_FLOOR_OLD_ESP,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_ESP,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_ESP,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_ES,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

SWE_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_SWE,
        "U_window": U_WINDOW_NEW_SWE,
        "U_floor": U_FLOOR_NEW_SWE,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_SWE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_SWE,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_SW,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_SWE,
        "U_window": U_WINDOW_OLD_SWE,
        "U_floor": U_FLOOR_OLD_SWE,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_SWE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_SWE,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_SW,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_SWE,
        "U_window": U_WINDOW_NEW_SWE,
        "U_floor": U_FLOOR_NEW_SWE,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_SWE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_SWE,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_SW,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_SWE,
        "U_window": U_WINDOW_OLD_SWE,
        "U_floor": U_FLOOR_OLD_SWE,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_SWE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_SWE,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_SW,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

BUL_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_BUL,
        "U_window": U_WINDOW_NEW_BUL,
        "U_floor": U_FLOOR_NEW_BUL,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_BUL,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_BUL,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_BU,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_BUL,
        "U_window": U_WINDOW_OLD_BUL,
        "U_floor": U_FLOOR_OLD_BUL,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_BUL,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_BUL,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_BU,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_BUL,
        "U_window": U_WINDOW_NEW_BUL,
        "U_floor": U_FLOOR_NEW_BUL,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_BUL,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_BUL,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_BU,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_BUL,
        "U_window": U_WINDOW_OLD_BUL,
        "U_floor": U_FLOOR_OLD_BUL,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_BUL,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_BUL,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_BU,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}


IT_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_IT_SFH,
        "U_window": U_WINDOW_NEW_IT_SFH,
        "U_floor": U_FLOOR_NEW_IT_SFH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_IT,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_IT,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_IT,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_IT_SFH,
        "U_window": U_WINDOW_OLD_IT_SFH,
        "U_floor": U_FLOOR_OLD_IT_SFH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_IT,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_IT,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_IT,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_IT_MFH,
        "U_window": U_WINDOW_NEW_IT_MFH,
        "U_floor": U_FLOOR_NEW_IT_MFH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_IT,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_IT,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_IT,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_IT_MFH,
        "U_window": U_WINDOW_OLD_IT_MFH,
        "U_floor": U_FLOOR_OLD_IT_MFH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_IT,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_IT,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_IT,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}


FR_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_FR_SFH,
        "U_window": U_WINDOW_NEW_FR_SFH,
        "U_floor": U_FLOOR_NEW_FR_SFH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_FR,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_FR,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_FR,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_FR_SFH,
        "U_window": U_WINDOW_OLD_FR_SFH,
        "U_floor": U_FLOOR_OLD_FR_SFH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_FR,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_FR,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_FR,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_FR_MFH,
        "U_window": U_WINDOW_NEW_FR_MFH,
        "U_floor": U_FLOOR_NEW_FR_MFH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_FR,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_FR,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_FR,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_FR_MFH,
        "U_window": U_WINDOW_OLD_FR_MFH,
        "U_floor": U_FLOOR_OLD_FR_MFH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_FR,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_FR,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_FR,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}

DE_HOUSE_TYPES = {
    "SFH after 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_NEW_DE_SFH,
        "U_window": U_WINDOW_NEW_DE_SFH,
        "U_floor": U_FLOOR_NEW_DE_SFH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_DE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_DE,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_DE,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "SFH before 2000": {
        "A_wall": AREA_WALL_SFH,
        "A_window": AREA_WINDOW_SFH,
        "A_floor": AREA_FLOOR_SFH,
        "U_wall": U_WALL_OLD_DE_SFH,
        "U_window": U_WINDOW_OLD_DE_SFH,
        "U_floor": U_FLOOR_OLD_DE_SFH,
        "height": HEIGHT_SFH,
        "cooling_cap": AC_CAPACITY_SFH,
        "heating_cap": HP_CAPACITY_SFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_SFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_DE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_DE,
        "battery_cap": BATTERY_STORAGE_SFH,
        "battery_throughput": BATTERY_THROUGHPUT_SFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_DE,
        "pv_area": AREA_COVERED_BY_PV_SFH
    },
    "MFH after 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_NEW_DE_MFH,
        "U_window": U_WINDOW_NEW_DE_MFH,
        "U_floor": U_FLOOR_NEW_DE_MFH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": TRIPLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_DE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_DE,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_DE,
        "pv_area": AREA_COVERED_BY_PV_MFH
    },
    "MFH before 2000": {
        "A_wall": AREA_WALL_MFH,
        "A_window": AREA_WINDOW_MFH,
        "A_floor": AREA_FLOOR_MFH,
        "U_wall": U_WALL_OLD_DE_MFH,
        "U_window": U_WINDOW_OLD_DE_MFH,
        "U_floor": U_FLOOR_OLD_DE_MFH,
        "height": HEIGHT_MFH,
        "cooling_cap": AC_CAPACITY_MFH,
        "heating_cap": HP_CAPACITY_MFH,
        "shgc": SINGLE_GLAZED,
        "perc_s_windows": WINDOWS_FACING_SOUTH,
        "people": PEOPLE_MFH,
        "v_rate": VENTILATON_RATE,
        "setpoint_ac": SETPOINT_AC_DE,
        "COP_ac" : AC_COP,
        "COP_hp" : HP_COP,
        "setpoint_hp": SETPOINT_HP_DE,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS,
        "pv_per_area": PV_2019_DE,
        "pv_area": AREA_COVERED_BY_PV_MFH
    }
}