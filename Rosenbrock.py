from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Figure for graph
figure = plt.figure()

# Subplot for 3D projection
ax = figure.add_subplot(projection = '3d')

# Get axes ranges for graph
x_axis = np.arange(-2, 2, 0.01)
y_axis = np.arange(-2, 2, 0.01)

# Create a meshgrid from axes vectors
x_axis, y_axis = np.meshgrid(x_axis, y_axis)

# Rosenbrock function
z_axis = (100 * (y_axis - x_axis**2)**2) + (x_axis - 1)**2

# Create plot surface for graph
surface = ax.plot_surface(x_axis, y_axis, z_axis, cmap = cm.coolwarm, linewidth = 1)
figure.colorbar(surface)

# Show graph
plt.title('Funcion Rosenbrock')
plt.show()
