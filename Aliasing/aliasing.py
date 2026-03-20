import matplotlib.pyplot as plt
import numpy as np

# recreating aliasing effect by generating 64 images of a propeller with 5 blades

M = 64
tm = np.linspace(-M/2, M/2, M+1)
x = np.linspace(0, 2*np.pi, 1000)

for m in tm:
  plt.polar(x, np.sin(5*x + ((m*np.pi)/10)))
  plt.pause(0.05)
    
