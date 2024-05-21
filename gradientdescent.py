from numpy import arange
from numpy import meshgrid
from matplotlib import pyplot

# objective function
def objective(x, y):
    return 0.1 * x**2.0 + 2 * y**2.0

# define range for input
r_min, r_max = -3.0, 3.0
# sample input range uniformly at 0.1 increments
xaxis = arange(r_min, r_max, 0.01)
yaxis = arange(r_min, r_max, 0.01)
# create a mesh from the axis
x, y = meshgrid(xaxis, yaxis)
# compute targets
results = objective(x, y)
# create a surface plot with the jet color scheme
figure = pyplot.figure()
axis = figure.add_subplot(projection="3d")
axis.plot_surface(x, y, results, cmap="ocean")
# show the plot
pyplot.show()
