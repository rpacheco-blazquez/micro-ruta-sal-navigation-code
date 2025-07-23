import numpy as np
import pandas as pd
import os
import funciones as f
import movements as m
import ship as sh
import matplotlib.pyplot as plt

velocity = np.linspace(0, 15, 100) 
direction = 45
time = np.linspace(0, 100, 100)  # Time from 0 to 10 seconds

alfa = np.zeros(len(time))  
rightning_moment = np.zeros(len(time))  
equilibrium = np.zeros(len(time)) 
heeling_moment = np.zeros(len(time))

for i in range(len(time)):
    vel = int(velocity[i])

    # Create a SAIL instance
    sail = sh.SAIL(speed=velocity[i])
    roll = m.ROLL()
  
    # Calculate lift and drag
    lift = sail.lift()  # Assuming alfa is 0 for this example
    drag = sail.drag()
    heeling_moment[i] = sail.heeling_moment()
   

    roll = m.ROLL()  # Example displacement
    alfa[i] = roll.solve_equilibrium(sail)
    rightning_moment[i] = roll.get_GZ(alfa[i]) * roll.displacement * 0.1 # Get GZ value for the current alfa
    heeling_moment[i] = sail.heeling_moment() * 0.1

plt.plot(time, alfa, label='List Angle (degrees)')
plt.plot(time, heeling_moment, label='Heeling Moment')
plt.plot(time, rightning_moment, label='Rightning Moment')
plt.grid(True)
plt.legend()
plt.xlabel('Time (s)')
plt.title('List Angle Over Time')
plt.grid() 
plt.show()
