import matplotlib.pyplot as plt
import numpy as np
# interpolation of a sin function

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y, color = 'hotpink')       # original sin function

def linear_interpolation(x, x_data, y_data):      # linear interpolation function
  y = np.zeros_like(x)
  for i in range(len(x)):
    id_a = 0
    id_b = 1
    while id_b <= len(x_data) - 1 and x[i] > x_data[id_b]:      # if x[i] is outside the current segment, change to the next, further one
      id_a += 1
      id_b += 1
    y[i] = y_data[id_a] + ((y_data[id_b] - y_data[id_a])*((x[i] - x_data[id_a])/(x_data[id_b] - x_data[id_a])))
  return y

x_nodes = np.linspace(0,2*np.pi, 10)
y_nodes = np.sin(x_nodes)
plt.scatter(x_nodes, y_nodes, color = 'darkorange')

y_interpolated = linear_interpolation(x, x_nodes, y_nodes)
y_interp = np.interp(x, x_nodes, y_nodes)                       # numpy interp function
plt.plot(x, y_interpolated, linestyle = 'dashdot', lw = 2)
#plt.plot(x, y_interp, linestyle = 'dashdot', color = 'ligthgreen')      # plot for numpy interp function
plt.show()