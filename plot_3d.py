# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.power((X**2 + Y**2),1/2)
# Plot the surface.
surf = ax.plot_surface(X, Y, R, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# Dot plot_surface
y_dot = np.linspace(10, -1, 6)
x_dot = np.linspace(-10, 2, 6)
r_dot = np.power((x_dot**2 + y_dot**2),1/2)
print(r_dot)
# Plot scatter
scat = ax.scatter(x_dot,y_dot,r_dot,'-ok')

# Customize the z axis.
ax.set_zlim(-5, 13)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
