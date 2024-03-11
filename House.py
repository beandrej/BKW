import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

air_density = 1.293  # [kg/m^3]
cp_air = 1005 * air_density  # [J/(m^3*K)]
cc_density = 800  # [kg/m^3]
cp_cc = 840 * cc_density  # [J/(m^3*K)]


class ACUnit:

    def __init__(self, power, setpoint, range, t_initial, cop=3.5):
        self.setpoint = setpoint
        self.range = range
        self.power = power
        self.lb = self.setpoint
        self.ub = self.setpoint + self.range
        self.t_initial = t_initial
        self.cop = cop
        self.ac_state = self.set_ac()

    def set_ac(self):
        if self.t_initial < self.lb:
            self.ac = 0
            return self.ac
        elif self.t_initial > self.ub:
            self.ac = 1
            return self.ac
        else:
            self.ac = 0
            return self.ac

    def control(self, t_in):

        if self.ub < t_in:
            self.ac_state = 1
        elif self.lb > t_in:
            self.ac_state = 0
        else:
            self.ac_state = 0.8 + (t_in - self.lb) / (self.ub - self.lb) * 0.2
        return self.ac_state

    def is_on(self):
        return self.ac_state == 1


class HeatPump:

    def __init__(self, power, setpoint, range, t_initial, cop=3.5):
        self.power = power
        self.setpoint = setpoint
        self.range = range
        self.lb = self.setpoint - self.range
        self.ub = self.setpoint
        self.t_initial = t_initial
        self.cop = cop
        self.hp_state = self.set_hp()

    def set_hp(self):
        if self.t_initial < self.lb:
            self.hp = 0
            return self.hp
        elif self.t_initial > self.ub:
            self.hp = 1
            return self.hp
        else:
            self.hp = 0
            return self.hp

    def control(self, t_in):
        if self.lb > t_in:
            self.hp_state = 1
        elif self.ub < t_in:
            self.hp_state = 0
        else:
            self.hp_state = 0.8 + (t_in - self.lb) / (self.ub - self.lb) * 0.2
        return self.hp_state

    def is_on(self):
        return self.hp_state == 1


class House:

    def __init__(
        self,
        A_wall,
        A_window,
        A_floor,
        U_wall,
        U_window,
        U_floor,
        height,
        cooling_cap,
        heating_cap,
        shgc,
        perc_s_windows,
        people,
        v_rate,
        setpoint_ac,
        setpoint_hp,
        shade_factor=0.7,
        t_initial=292,
        t_des=295,
        wall_th=0.1,
    ):

        self.A_wall = A_wall  # [m^2]
        self.A_window = A_window  # [m^2]
        self.A_floor = A_floor  # [m^2]
        self.U_wall = U_wall  # [W/(m^2*K)]
        self.U_window = U_window  # [W/(m^2*K)]
        self.U_floor = U_floor  # [W/(m^2*K)]
        self.height = height  # [m]
        self.cooling_cap = cooling_cap  # [W]
        self.heating_cap = heating_cap  # [W]
        self.shgc = shgc
        self.people = people
        self.windows_s = perc_s_windows * self.A_window
        self.v_rate = v_rate
        self.shade_factor = shade_factor
        self.setpoint_ac = setpoint_ac
        self.setpoint_hp = setpoint_hp
        self.t_dev = 1
        self.t_des = t_des
        self.t_initial = t_initial
        self.wall_th = wall_th
        self.ac = ACUnit(cooling_cap, self.setpoint_ac, self.t_dev, self.t_initial)
        self.hp = HeatPump(heating_cap, self.setpoint_hp, self.t_dev, self.t_initial)
        self.inertia = self.set_inertia()

    def set_inertia(self):  # [J/K]
        air_term = cp_air * self.A_floor * self.height
        cc_term = cp_cc * self.A_wall * self.wall_th
        return air_term + cc_term

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

    def run_scenario(self):
        years = self.scenario["years"]
        increase_temp = self.scenario["temp_develop"]
        output_dictionary = {}
        for idx, year in enumerate(years):
            self.t_outside = [t + increase_temp[idx] for t in self.t_outside] # abs T increase
            output_dictionary[year] = self.run()
        return output_dictionary

    def run(self):
        e_demand_list_AC = [self.house.ac.ac_state]
        e_demand_list_HP = [self.house.hp.hp_state]
        t_list = [self.house.t_initial]

        for idx, t in enumerate(self.t_outside):
            t_next = t_list[idx] + self.house.get_t_diff(
                self.timestep, t, t_list[idx], self.irr_list[idx]
            )
            t_list.append(t_next)

            e_demand_list_AC.append(self.house.cooling_cap * self.house.ac.ac_state)
            e_demand_list_HP.append(self.house.heating_cap * self.house.hp.hp_state)

        tot_demand_AC = sum(e_demand_list_AC) / self.house.ac.cop

        return t_list, e_demand_list_AC, tot_demand_AC


class Plot_output:
    def __init__(self, output_dictionary, PV_output, t_des=295):
        self.output = output_dictionary
        self.hours_in_year = list(np.arange(0, 8761, 1))
        self.days_in_year = [i / 24 for i in self.hours_in_year]
        self.t_des = t_des
        self.PV_output = PV_output

    def plot_base_case_with_PV(self):
        years = list(self.output.keys())
        net_demand = [a - b for a, b in zip(self.output[years[0]][1], self.PV_output)]
        plt.plot(self.days_in_year[1:], net_demand)
        plt.xlabel("Days in year")
        plt.ylabel("Net Demand [W]")
        plt.title("Net Demand")
        plt.show()

    def plot_temperature_scenario(self, window):
        for year in self.output:
            days_df = pd.DataFrame(self.days_in_year, columns=['hours'])
            temp_df = pd.DataFrame(self.output[year][0], columns=['temp'])
            roll_days = days_df['hours'].rolling(window=window).mean()
            roll_temp = temp_df['temp'].rolling(window=window).mean()
            plt.plot(
                roll_days,
                roll_temp,
                label="SFH after 2000 " + str(year),
            )
        plt.axhline(y=self.t_des, color="r", linestyle="dotted", label="T_desired")
        plt.xlabel("Days in year")
        plt.ylabel("Temperature [K]")
        plt.title("Inside temperature of the house")
        plt.legend()
        plt.show()

    def plot_temp_compare(self, window):
        for house_type in self.output:
            days_df = pd.DataFrame(self.days_in_year, columns=['hours'])
            temp_df = pd.DataFrame(self.output[house_type][0], columns=['temp'])
            roll_days = days_df['hours'].rolling(window=window).mean()
            roll_temp = temp_df['temp'].rolling(window=window).mean()
            plt.plot(
                roll_days,
                roll_temp,
                label=str(house_type)
            )
        plt.axhline(y=self.t_des, color="r", linestyle="dotted", label="T_desired")
        plt.xlabel("Days in year")
        plt.ylabel("Temperature [K]")
        plt.title("Inside temperature of the house")
        plt.legend()
        plt.show()
        
        

    def plot_ac_demand(self):
        for year in self.output:
            plt.plot(
                self.days_in_year,
                self.output[year][1],
                label="SFH after 2000 " + str(year),
            )
            # plt.plot(days_in_year, T_SFH_before, label='SFH before 2000')
        # plt.axhline(y=t_des, color='r', linestyle='dotted', label='T_desired')
        plt.xlabel("Days in year")
        plt.ylabel("Demand [W]")
        plt.title("Cooling Demand")
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


class PV:
    def __init__(self, path):
        self.PV_data = pd.read_csv(path, header=None)
        self.PV_output = list(self.PV_data.iloc[:, 1])

    def return_PV_list(self):
        return self.PV_output
