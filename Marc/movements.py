import pandas as pd
import os
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.optimize import root_scalar
from scipy.integrate import solve_ivp

class ROLL:     
    def __init__(self):
        self.displacement = 200  # in N
        self.gz_df = self.gz_data()  # cache the dataframe here
        self.I = 2000               # momento de inercia 
        self.c = 2000             # amortiguamiento 
        

    def gz_data(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'GZ.csv') 
        df = pd.read_csv(file_path, sep=';')
        df.sort_values(by='angle', inplace=True)
        return df
    
    def get_GZ(self, theta):
        return np.interp(theta, self.gz_df['angle'], self.gz_df['GZ'])
        
    def equilibrium_function(self, theta, sail):
        M_heel = sail.heeling_moment()
        M_right = self.displacement * self.get_GZ(theta)
        return M_right - M_heel
    
    def solve_equilibrium(self, sail, search_range=(0, 60.0)):
        a, b = search_range
        f_a = self.equilibrium_function(a, sail)
        f_b = self.equilibrium_function(b, sail)

        # First try finding a real root if signs are different
        if f_a * f_b < 0:
            result = root_scalar(
                self.equilibrium_function,
                args=(sail,),
                bracket=search_range,
                method='brentq'
            )
            if result.converged:
                return result.root

        # Fallback: minimize the absolute value (get as close to 0 as possible)
        result = minimize_scalar(
            lambda theta: abs(self.equilibrium_function(theta, sail)),
            bounds=search_range,
            method='bounded'
        )

        if result.success:
            if result.fun > 0.1:  # abs(equilibrium_function) is too large
                return 90
        
            return result.x
        return None

    def roll_dynamics(self, t, y, sail):
        theta, omega = y  # y[0]=θ (angle), y[1]=θ̇ (angular velocity)
        M_restoring = -self.displacement * self.get_GZ(theta)
        M_heeling = sail.heeling_moment(t)
        domega_dt = (M_heeling + M_restoring - self.c * omega) / self.I
        return [omega, domega_dt]

    def solve_roll_dynamics(self, sail, theta0=0.0, omega0=0.0, t_span=(0, 100), dt=0.1):
        t_eval = np.arange(t_span[0], t_span[1], dt)
        sol = solve_ivp(
            fun=lambda t, y: self.roll_dynamics(t, y, sail),
            t_span=t_span,
            y0=[theta0, omega0],
            t_eval=t_eval,
            method='RK45'
        )
        return sol


   


