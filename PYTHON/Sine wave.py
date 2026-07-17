#importing modules
import numpy as np
import matplotlib.pyplot as plt
# Initializing Variables
A = 5
omega = 10
t = np.linspace(0,10,1000)
#equation
x = A*np.sin(omega*t)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

