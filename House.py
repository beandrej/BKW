import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt

def read_PV(path):
    df = pd.read_csv(path)
    data = df.iloc[:, 1].to_list()
    return data

def rolling_window(list, window):
    df = pd.DataFrame(list, columns=['x'])
    return df['x'].rolling(window=window).mean()

# -------------- CONSTANTS -------------

HEAT_CAPACITY_AIR = 1005 # [J/(kg*K)] 
HEAT_CAPACITY_CC = 840 # [J/(kg*K)]
DENSITY_AIR = 1.293 # [kg/m3]
DENSITY_CC = 800 # [kg/m3]

CP_AIR =  HEAT_CAPACITY_AIR * DENSITY_AIR # [J/(m3*K)]
CP_CC = HEAT_CAPACITY_CC * DENSITY_CC # [J/(m3*K)]

HOURS_IN_YEAR = np.arange(0, 8760, 1)
DAYS_IN_YEAR = [i / 24 for i in HOURS_IN_YEAR]

# ----------------- Set AC/HP -----------------------

COP_AC = 3.5
COP_HP = 3.5

# increase of control in temperature range [K]
OPERATION_RANGE_HP = 0.2
OPERATION_RANGE_AC = 0.2

# ----------------- PV Data -------------------------

PV_PROD_LIST = read_PV('PV_data/PVoutput_2019.csv')

class ACUnit:

    def __init__(self, power, setpoint, t_initial):
        self.setpoint = setpoint #desired temperature [K]
        self.power = power # power [W]
        self.t_initial = t_initial # initial temp [K]
        self.COP = COP_AC # coefficient of performance

        # linear increase range
        self.lowerbound = self.setpoint 
        self.upperbound = self.setpoint + OPERATION_RANGE_AC
        self.init = self.init_ac() # initialize on/off mode

    def init_ac(self):
        if self.t_initial > self.upperbound: 
            return 1
        else:
            return 0
        
    # Controller 0%, 50%, 80%, 100%   
    def control(self, t_in):
        if t_in > self.upperbound:
            self.output = 1 # 100%
        elif t_in < self.lowerbound:
            self.output = 0 # 0%
        else:  
            if (t_in - self.lowerbound) / (self.upperbound - self.lowerbound) >= 0.5: # when in upper 50% of temp range
                self.output = 0.8 # set output to 80%
            else:
                self.output = 0.5 # set output to 50%
        return self.output

    def is_on(self):
        return self.output > 0

class HeatPump:

    def __init__(self, power, setpoint, t_initial):
        self.setpoint = setpoint
        self.power = power
        self.t_initial = t_initial
        self.COP = COP_HP

        # linear increase range
        self.lowerbound = self.setpoint - OPERATION_RANGE_HP
        self.upperbound = self.setpoint
        self.output = self.init_hp()

    def init_hp(self):
        if self.t_initial < self.lowerbound: 
            return 0 
        else:
            return 1

    # Controller 0%, 50%, 80%, 100%
    def control(self, t_in):
        if t_in < self.lowerbound:
            self.output = 1 # 100%
        elif t_in > self.upperbound:
            self.output = 0 # 0%
        else:  
            if (t_in - self.lowerbound) / (self.upperbound - self.lowerbound) <= 0.5: # when in lower 50% of temp range
                self.output = 0.8 # set output to 80%
            else:
                self.output = 0.5 # set output to 50%
        return self.output

    def is_on(self):
        return self.output > 0

class Battery:
    def __init__(self, capacity, throughput):
        self.capacity = capacity # Max capacity [Wh]
        self.throughput = throughput # Max charging/discharge rate in Volt * Ampere [W]
        self.flow = 0 # Current amout of energy flowing in/out [W]
        self.soc = self.capacity # Current amount of energy in the battery [Wh]

    def charge(self, input):
        previous_soc = self.soc
        self.flow = input

        if self.throughput < input: # check if input is too big
            self.flow = self.throughput

        if self.capacity > self.soc: # charge battery if there is available capacity
            self.soc += self.flow
            
        elif self.soc > self.capacity: # if battery got "overcharged", set to max capacity
            self.flow = self.capacity - previous_soc
            self.soc = self.capacity
        
        else: # battery is full
            self.soc = self.capacity
            self.flow = 0

    def discharge(self, output):
        previous_soc = self.soc
        self.flow = -output

        if self.throughput < output: # check if output is too big
            self.flow = -self.throughput

        if self.soc > 0: # discharge battery
            self.soc += self.flow
        
        elif self.soc < 0: # if battery got "undercharged", set to 0
            self.flow = -previous_soc
            self.soc = 0

        else: # if battery is already empty
            self.flow = 0
            self.soc = 0
    
    def is_full(self):
        return self.capacity == self.soc
    
    def is_empty(self):
        return self.soc == 0

class House:

    def __init__(
        self,
        A_wall, # Wall area [m2]
        A_window, # Window area [m2]
        A_floor, # Floor area [m2]
        U_wall, # Wall resistance [W/(m2*K)]
        U_window, # Window resistance [W/(m2*K)]
        U_floor, # Floor resistance [W/(m2*K)]
        height, # Heigh [m2]
        cooling_cap, # AC capacity
        heating_cap, # HP capacity
        shgc, # Solar heat gain coefficient of windows [0 to 1]
        perc_s_windows, # Percentage of windows facing south [0 to 1]
        people, # People in house
        v_rate, # Venitaltion rate per hour [0 to 1] (little influence)
        setpoint_ac, # Desired AC temp [K]
        setpoint_hp, # Desired HP temp [K]
        battery_cap, # Battery capacity [Wh]
        battery_throughput, # Battery throughput [W]
        shade_factor=0.7,
        t_initial=295,
        wall_th=0.1,
    ):

        self.A_wall = A_wall  
        self.A_window = A_window  
        self.A_floor = A_floor  
        self.U_wall = U_wall  
        self.U_window = U_window  
        self.U_floor = U_floor  
        self.height = height  
        self.cooling_cap = cooling_cap 
        self.heating_cap = heating_cap 
        self.shgc = shgc
        self.people = people
        self.windows_s = perc_s_windows * self.A_window
        self.v_rate = v_rate
        self.shade_factor = shade_factor
        self.setpoint_ac = setpoint_ac
        self.setpoint_hp = setpoint_hp
        self.t_initial = t_initial
        self.wall_th = wall_th
        self.battery_cap = battery_cap
        self.battery_throughput = battery_throughput
        self.ac = ACUnit(cooling_cap, self.setpoint_ac, self.t_initial)
        self.hp = HeatPump(heating_cap, self.setpoint_hp, self.t_initial)
        self.battery = Battery(self.battery_cap, self.battery_throughput)
        self.inertia = self.set_inertia()

    # calculate inertia of house
    def set_inertia(self):  # [J/K]
        air_term = CP_AIR * self.A_floor * self.height
        cc_term = CP_CC * self.A_wall * self.wall_th
        return air_term + cc_term

    # calculate first part of heatgain
    def get_heatgain(self, t_out, t_in, solar_irr):  # [W], heat gain per timestep
        heat_gain = (
            self.A_wall * self.U_wall
            + self.A_window * self.U_window
            + self.A_floor * self.U_floor
            + self.v_rate / 3600 * self.A_floor
        ) * (t_out - t_in)
        solar_term = self.shgc * self.windows_s * solar_irr * (1 - self.shade_factor)
        people_term = self.people * 100  # 100[W] per person
        return heat_gain + solar_term + people_term

    # delta for next temperature value
    def get_t_diff(self, timestep, t_out, t_in, solar):  # [K]
        t_diff = (
            (self.get_heatgain(t_out, t_in, solar) * timestep / self.inertia)
            - (self.ac.control(t_in) * self.cooling_cap * timestep / self.inertia)
            + (self.hp.control(t_in) * self.heating_cap * timestep / self.inertia)
        )
        return t_diff
    
class RunSimulation:

    def __init__(self, house, t_outside, irr_list, timestep, scenario={}):
        self.house = house
        self.t_outside = t_outside
        self.irr_list = irr_list
        self.timestep = timestep
        self.scenario = scenario

    # smoothing outside temperature #TODO function isn't working properly (different outputs for same house)
    def temperature_smoothing(self):
        #split temperature data into days
        T_days = np.split(self.t_outside, range(24, 8760, 24))
        #take the average of each day
        T_days_avg = [np.mean(day) for day in T_days]
        #indices
        idx = list(range(0, 8760, 24))
        idx += [len(self.t_outside)+1]
        for i,day in enumerate(T_days):
            if i == 0:
                self.t_outside[idx[i]:idx[i+1]] = [T_days_avg[i]]*24
            elif i == 1:
                self.t_outside[idx[i]:idx[i+1]] = [(T_days_avg[i] + 0.5 * T_days_avg[i-1]) / 1.5]*24
            elif i == 2:
                self.t_outside[idx[i]:idx[i+1]] = [(T_days_avg[i] + 0.5 * T_days_avg[i-1] + 0.25 * T_days_avg[i-2]) / 1.75]*24
            else:
                self.t_outside[idx[i]:idx[i+1]] = [(T_days_avg[i] + 0.5 * T_days_avg[i-1] + 0.25 * T_days_avg[i-2] + 0.125 * T_days_avg[i-3]) / 1.875]*24
        #print(self.t_outside)

    # main calculation
    def run(self):
        AC_consumption = [self.house.ac.init_ac() * self.house.cooling_cap]
        HP_consumption = [self.house.hp.init_hp() * self.house.cooling_cap]
        net_demand = [0]
        SOC_battery = [0]
        flow_battery = [0]
        t_inside = [self.house.t_initial]

        
        #smooth temperature to consider the inertia of the house
        #self.temperature_smoothing()

        for idx, t in enumerate(self.t_outside):
            t_next = t_inside[idx] + self.house.get_t_diff(
                self.timestep, t, t_inside[idx], self.irr_list[idx]
            )
            t_inside.append(t_next)

            cooling_needed = self.house.cooling_cap * self.house.ac.control(t_inside[idx])
            AC_consumption.append(cooling_needed)
            heating_needed = self.house.heating_cap * self.house.hp.control(t_inside[idx])
            HP_consumption.append(heating_needed)
            overproduction = PV_PROD_LIST[idx] - cooling_needed

            # Battery storage interacting with PV prodcution
            # Battery charge and discharge cycles
            if overproduction > 0:
                net_demand.append(0)

                if self.house.battery.is_full():
                    SOC_battery.append(self.house.battery.capacity)
                    flow_battery.append(0)
                else:
                    self.house.battery.charge(overproduction)
                    SOC_battery.append(self.house.battery.soc)
                    flow_battery.append(self.house.battery.flow)

            elif overproduction < 0:

                if self.house.battery.is_empty():
                    net_demand.append(abs(overproduction))
                    SOC_battery.append(0)
                    flow_battery.append(0)
                else:
                    self.house.battery.discharge(abs(overproduction))
                    net_demand.append(abs(overproduction) - abs(self.house.battery.flow))
                    SOC_battery.append(self.house.battery.soc)
                    flow_battery.append(self.house.battery.flow)

            else: 
                net_demand.append(0)
                flow_battery.append(0)
                SOC_battery.append(self.house.battery.soc)

        # delete initializing value (mostly 0)
        t_inside.pop(0)
        AC_consumption.pop(0)
        SOC_battery.pop(0)
        flow_battery.pop(0)
        net_demand.pop(0)
        HP_consumption.pop(0)

        return t_inside, AC_consumption, SOC_battery, flow_battery, net_demand, HP_consumption

    # run screnarios for future years
    def run_scenario(self):
        years = self.scenario["years"]
        increase_temp = self.scenario["temp_develop"]
        output_dictionary = {}
        for idx, year in enumerate(years):
            self.t_outside = [t + increase_temp[idx] for t in self.t_outside] # abs T increase
            output_dictionary[year] = self.run()
        return output_dictionary


# plot class, define different plots

class Plot_output:

    def __init__(self, output_dictionary, PV_output, t_des=295):
        self.output = output_dictionary
        self.t_des = t_des
        self.PV_output = PV_output

    def plt_net_demand(self):
        for house_type in self.output:
            net_demand = self.output[house_type][4]
            plt.plot(DAYS_IN_YEAR, net_demand, label=str(house_type))

        plt.xlabel("Time [days]")
        plt.ylabel("Net Cooling Demand [Wh]")
        plt.title("Net cooling demand with batteries installed")
        plt.legend()
        plt.show()

    def plt_ac_consumption(self):
        for house_type in self.output:
            ac_consumption = self.output[house_type][1]
            plt.plot(DAYS_IN_YEAR, ac_consumption, label=str(house_type))

        plt.xlabel("Time [days]")
        plt.ylabel("AC consumption [Wh]")
        plt.title("Air conditioner electricity consumption")
        plt.legend()
        plt.show()

    def plt_flow_battery(self, window):
        for house_type in self.output:
            flow_battery = pd.DataFrame(self.output[house_type][3]).rolling(window=window).mean()
            plt.plot(DAYS_IN_YEAR, flow_battery, label=str(house_type))

        plt.xlabel("Time [days]")
        plt.ylabel("Battery flow [W]")
        plt.title("Flows in/out of battery")
        plt.legend()
        plt.show()

    def plt_SOC_battery(self, window):
        for house_type in self.output:
            soc_battery = pd.DataFrame(self.output[house_type][2]).rolling(window=window).mean()
            plt.plot(DAYS_IN_YEAR, soc_battery, label=str(house_type))

        plt.xlabel("Time [days]")
        plt.ylabel("Battery SOC [Wh]")
        plt.title("Battery State of Charge")
        plt.legend()
        plt.show()

    def plot_base_case_with_PV(self):
        years = list(self.output.keys())
        net_demand = [a - b for a, b in zip(self.output[years[0]][1], self.PV_output)]
        plt.plot(DAYS_IN_YEAR, net_demand)
        plt.xlabel("Days in year")
        plt.ylabel("Net Demand [W]")
        plt.title("Net Demand")
        plt.show()

    def plot_temperature_scenario(self, window):
        for year in self.output:
            days_df = pd.DataFrame(DAYS_IN_YEAR, columns=['hours'])
            temp_df = pd.DataFrame(self.output[year][0], columns=['temp'])
            roll_days = days_df['hours'].rolling(window=window).mean()
            roll_temp = temp_df['temp'].rolling(window=window).mean()
            plt.plot(
                roll_days,
                roll_temp,
                label="MFH after 2000 " + str(year),
            )
        plt.axhline(y=self.t_des, color="r", linestyle="dotted", label="T_desired")
        plt.xlabel("Days in year")
        plt.ylabel("Temperature [K]")
        plt.title("Inside temperature of the house")
        plt.legend()
        plt.show()

    def plt_t_inside(self, window, setpoint_ac, setpoint_hp):
        for house_type in self.output:
            t_inside = pd.DataFrame(self.output[house_type][0]).rolling(window=window).mean()
            plt.plot(DAYS_IN_YEAR, t_inside, label=str(house_type))

        plt.axhline(y=setpoint_ac, color="r", linestyle="dotted", label="AC threshold")
        plt.axhline(y=setpoint_hp, color="b", linestyle="dotted", label="HP threshold")
        plt.xlabel("Time [days]")
        plt.ylabel("Temperature [K]")
        plt.title("Inside temperature of the house")
        plt.legend()
        plt.show()

    def plot_aggregated_ac_demand_over_years(self):
        total_demand_list = []
        years = []
        for year in self.output:
            total_demand_list += [self.output[year][2]]
            years += [int(year)]

        plt.plot(years, total_demand_list)
        plt.xlabel("Year")
        plt.ylabel("Aggregated Demand")
        plt.title("Evolution of Cooling Demand")
        plt.show()

    def bar_plot_ac_consumption(self):

        categories = ['Cooling demand']
        houses = list(self.output.keys())
        bar_width = 0.15
        index = np.arange(len(categories))

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, house in enumerate(houses):
            data = [sum(self.output[house][1]) / (1e3 * 3.5)]
            ax.bar(index + i * bar_width, data, bar_width, label=house)

        ax.set_xlabel('House Types')
        ax.set_ylabel('Cooling demand [kWh]')
        ax.set_title('Aggregated Cooling Demand')
        ax.set_xticks(index + bar_width * (len(houses) - 1) / 2)
        ax.set_xticklabels(categories)
        ax.legend()

        plt.tight_layout()
        plt.show()

    def bar_plot_net_demand(self):

        categories = ['Net Demand']
        houses = list(self.output.keys())
        bar_width = 0.15
        index = np.arange(len(categories))

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, house in enumerate(houses):
            data = [sum(self.output[house][4]) / (1e3 * 3.5)]
            ax.bar(index + i * bar_width, data, bar_width, label=house)

        ax.set_xlabel('House Types')
        ax.set_ylabel('Net Cooling Demand [kWh]')
        ax.set_title('Aggregated Net Cooling Demand')
        ax.set_xticks(index + bar_width * (len(houses) - 1) / 2)
        ax.set_xticklabels(categories)
        ax.legend()

        plt.tight_layout()
        plt.show()
    
#pv input
class PV:
    def __init__(self, path):
        self.PV_data = pd.read_csv(path, header=None)
        self.PV_output = list(self.PV_data.iloc[:, 1])

    def return_PV_list(self):
        return self.PV_output
