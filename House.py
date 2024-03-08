
air_density = 1.293 #[kg/m^3]
cp_air = 1005*air_density #[J/(m^3*K)]
t_initial = 293
t_des = 286
delta_t_des = 1
ac_range = 1

lower_bound = t_des - delta_t_des
upper_bound = t_des + delta_t_des + ac_range

class ACUnit:
    def __init__(self, power):
        self.setpoint = t_des
        self.delta_t_des = delta_t_des
        self.ac_state =  self.set_ac()
        self.power = power

    def set_ac(self):
        if t_initial < lower_bound:
            self.ac = 0
            return self.ac
        elif t_initial > upper_bound:
            self.ac = 1
            return self.ac
        else:
            self.ac = 0
            return self.ac

    def control(self, t_in):

        if upper_bound > t_in:
            self.ac_state = 1
        elif lower_bound < t_in:
            self.ac_state = 0
        else:
            self.ac_state = (t_in - lower_bound) / (upper_bound - lower_bound)
        return self.ac_state


    def is_on(self):
        return self.ac_state == 1


class House:

    def __init__(self, A_wall, A_window, A_floor, U_wall, U_window, U_floor,
                 height, cooling_cap, shgc, perc_s_windows, people, v_rate):


        self.A_wall = A_wall #[m^2]
        self.A_window = A_window #[m^2]
        self.A_floor = A_floor #[m^2]
        self.U_wall = U_wall #[W/(m^2*K)]
        self.U_window = U_window #[W/(m^2*K)]
        self.U_floor = U_floor #[W/(m^2*K)]
        self.height = height #[m]
        self.cooling_cap = cooling_cap #[W]
        self.ac = ACUnit(cooling_cap)
        self.inertia = self.set_inertia()
        self.shgc = shgc
        self.people = people
        self.windows_s = perc_s_windows * self.A_window
        self.v_rate = v_rate

    def set_inertia(self): #[J/K]
        air_term = cp_air * self.A_floor*0.5 * self.height
        return air_term

    def get_heatgain(self, t_out, t_in, solar_irr): # [J], heat gain per timestep
        heat_gain = (self.A_wall * self.U_wall + self.A_window * self.U_window + self.A_floor * self.U_floor + self.v_rate * self.A_floor) * (t_out - t_in)
        solar_term = self.shgc * self.windows_s * solar_irr
        people_term = self.people * 100          # 100[W] per person
        return heat_gain + solar_term*0.5 + people_term


    def get_t_diff(self, timestep, t_out, t_in, solar): #[K]
        t_diff = (self.get_heatgain(t_out, t_in, solar)*timestep / self.inertia) - (
                  self.ac.control(t_in)*self.cooling_cap*timestep / self.inertia)
        return t_diff

