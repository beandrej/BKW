""" --------- SET HOUSE PARAMETERS ---------- """

# ---------- SAME FOR ALL HOUSES -------------

WALL_THICKNESS = 0.3 # Wall thickness [m]
VENTILATON_RATE = 0.7 # Ventilation rate [1/h] (little impact)
T_INITIAL = 295 # Initial Temperature inside the house [K]

WINDOWS_SHADE_FACTOR = 0.7 # Shading factor of windows [0 to 1]
WINDOWS_FACING_SOUTH = 0.35 # Percentage of windows facing south [0 to 1]

# ---------------- AC / HP / BATTERY ---------------------

AC_CAPACITY_SFH = 4000 # Air conditioner capacity for Single family house (SFH) [W]
AC_CAPACITY_MFH = 6000 # Air conditioner capacity for Multi family house (MFH) [W]

HP_CAPACITY_SFH = 8000 # Heat pump capacity for Single family house (SFH) [W]
HP_CAPACITY_MFH = 12000 # Heat pump capacity for Multi family house (MFH) [W]

BATTERY_STORAGE_SFH = 10000 # Battery storage for Single family house (SFH) [Wh]
BATTERY_STORAGE_MFH = 15000 # Battery storage for Multi family house (MFH) [Wh]

BATTERY_THROUGHPUT_SFH = 2000 # Battery throughput for Single family house (SFH) [W]
BATTERY_THROUGHPUT_MFH = 3000 # Battery throughput for Multi family house (MFH) [W]

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

""" -------------------- COUNTRY SPECIFIC VALUES ---------------------- """

# -------------------------- SWITZERLAND ----------------------------

U_WALL_NEW_CH = 0.2 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_CH = 0.63 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_CH = 1.2 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_CH = 2.7 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_CH = 0.3 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_CH = 1.2 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_CH = 273 + 24
SETPOINT_HP_CH = 273 + 18

# --------------------------- SPAIN --------------------------------

U_WALL_NEW_ESP = 2.04 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_ESP = 2.81 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_ESP = 8.24 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_ESP = 8.89 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_ESP = 1.39 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_ESP = 1.96 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_ESP = 273 + 27
SETPOINT_HP_ESP = 273 + 18

# --------------------------- SWEDEN -------------------------------

U_WALL_NEW_SWE = 0.85 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_SWE = 0.99 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_SWE = 3.84 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_SWE = 4.07 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_SWE = 0.78 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_SWE = 0.79 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_SWE = 273 + 24
SETPOINT_HP_SWE = 273 + 18

# -------------------------- BULGARIA -----------------------------

U_WALL_NEW_BUL = 0.75 # Wall thermal resistance [W/(m2*K)]
U_WALL_OLD_BUL = 1.65 # Wall thermal resistance [W/(m2*K)]

U_WINDOW_NEW_BUL = 3.85 # Window thermal resistance [W/(m2*K)]
U_WINDOW_OLD_BUL = 4.33 # Window thermal resistance [W/(m2*K)]

U_FLOOR_NEW_BUL = 0.45 # Floor thermal resistance [W/(m2*K)]
U_FLOOR_OLD_BUL = 1.39 # Floor thermal resistance [W/(m2*K)]

SETPOINT_AC_BUL = 273 + 24
SETPOINT_HP_BUL = 273 + 18

# ------------------------------------------------------------------

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
        "setpoint_hp": SETPOINT_HP_ESP,
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
        "setpoint_hp": SETPOINT_HP_ESP,
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
        "setpoint_hp": SETPOINT_HP_ESP,
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
        "setpoint_hp": SETPOINT_HP_ESP,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
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
        "setpoint_hp": SETPOINT_HP_SWE,
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
        "setpoint_hp": SETPOINT_HP_SWE,
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
        "setpoint_hp": SETPOINT_HP_SWE,
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
        "setpoint_hp": SETPOINT_HP_SWE,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
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
        "setpoint_hp": SETPOINT_HP_BUL,
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
        "setpoint_hp": SETPOINT_HP_BUL,
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
        "setpoint_hp": SETPOINT_HP_BUL,
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
        "setpoint_hp": SETPOINT_HP_BUL,
        "battery_cap": BATTERY_STORAGE_MFH,
        "battery_throughput": BATTERY_THROUGHPUT_MFH,
        "shade_factor": WINDOWS_SHADE_FACTOR,
        "t_initial": T_INITIAL,
        "wall_th": WALL_THICKNESS
    }
}
