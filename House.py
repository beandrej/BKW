
air_density = 1.293 #[kg/m^3]
cp_air = 1005*air_density #[J/(m^3*K)]

class House:

    t_initial = 300
    t_des = 300
    delta_t_des = 1


    def __init__(self, A_wall, A_window, A_floor, U_wall, U_window, U_floor, 
                 height, cooling_cap):


        self.A_wall = A_wall #[m^2]
        self.A_window = A_window #[m^2]
        self.A_floor = A_floor #[m^2]
        self.U_wall = U_wall #[W/(m^2*K)]
        self.U_window = U_window #[W/(m^2*K)]
        self.U_floor = U_floor #[W/(m^2*K)]
        self.height = height #[m]
        self.cooling_cap = cooling_cap #[W]
        self.ac = self.set_ac()
        self.inertia = self.set_inertia()

    def set_ac(self):

        if self.t_initial < self.t_des - self.delta_t_des:
            self.ac = 0
            return self.ac
        elif self.t_initial > self.t_des + self.delta_t_des:
            self.ac = 1
            return self.ac
        else:
            self.ac = 0
            return self.ac

    def set_inertia(self): #[J/K]
        return cp_air * self.A_floor * self.height



    def get_heatgain(self, t_out, t_in): # [J], heat gain per timestep
        heat_gain = (self.A_wall * self.U_wall + self.A_window * self.U_window + self.A_floor * self.U_floor) * (t_out - t_in)
        #solar_term = 0
        return heat_gain

    def ac_mode(self, t_in): #[0 or 1]

        if t_in < self.t_des - self.delta_t_des:
            self.ac = 0
            return self.ac
        elif t_in > self.t_des + self.delta_t_des:
            self.ac = 1
            return self.ac
        else:
            return self.ac


    def get_t_diff(self, timestep, t_out, t_in): #[K]
        t_diff = (self.get_heatgain(t_out, t_in)*timestep / self.inertia) - (
                  self.ac_mode(t_in)*self.cooling_cap*timestep/self.inertia) # PID Regler
        return t_diff
    