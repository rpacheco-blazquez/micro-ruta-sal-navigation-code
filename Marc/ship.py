import numpy as np
import pandas as pd
import os
import funciones as f

class SAIL:
    def __init__(self, speed):
        self.speed = speed # Wind speed
        self.area = 3.711530894
        self.alfa = 10  
        self.Cl() 
        self.Cd() 
        self.CG_sail = 1.245172527 + 0.4 #CG of the sail
        self.weight = -3 # Weight of the sail in N
        self.beta = 30 # Rotation of the sail arround the z axis in degrees
    
    def Cd(self): 
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'Cl_Cd_Sail.csv')
        df = pd.read_csv(file_path, header=None, sep=';')

        df[0] = pd.to_numeric(df[0], errors='coerce')

        column = df[df[0] == self.alfa]
        if column.empty:
            raise ValueError(f"No se encontró el ángulo {self.alfa} en el archivo.")
        self.Cd = float(column.iloc[0, 2])

    def Cl(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'Cl_Cd_Sail.csv')
        df = pd.read_csv(file_path, header=None, sep=';')

        df[0] = pd.to_numeric(df[0], errors='coerce')

        column = df[df[0] == self.alfa]
        if column.empty:
            raise ValueError(f"No se encontró el ángulo {self.alfa} en el archivo.")
        self.Cl = float(column.iloc[0, 1])
    
    def lift(self): #Beta = 90 - alfa (list)
        if self.Cl is None:
            raise ValueError("C_l no ha sido cargado.")
        else:
            rot = [0, 0, 0]
            rot[2] += self.beta - 90 #The direction of the lift force is perpendicular to the sail
        return 0.5 * 1.2 * self.Cl * self.area * (self.speed ** 2) * f.loc2glob([1,0,0], rot)
    
    def drag(self):
        if self.Cd is None:
            raise ValueError("C_D no ha sido cargado.")
        return 0.5 * 1.2 * self.Cd * self.area * (self.speed ** 2) * f.loc2glob([-1, 0, 0], [0, 0, self.beta])
    
    def heeling_moment(self, t=None):
        heeling_moments = self.lift()[1] * self.CG_sail + self.drag()[1] * self.CG_sail
        return heeling_moments
    
    
class HULL:
    def __init__(self, C_D, A):
        self.C_D = C_D
        self.A = A

    def drag(self, speed):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'Cl_Cd_Sail.csv')
        df = pd.read_csv(file_path, header=None, sep=';')
        column = df[df[0] == self.alfa]
        if column.empty:
            raise ValueError(f"No se encontró el ángulo {self.alfa} en el archivo.")
        self.Cd = float(column.iloc[0, 2])



    

    
