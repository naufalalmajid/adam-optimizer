import numpy as np
import matplotlib.pyplot as plt


# obj func
def obj(x, y):
    return x**2 + 2 * y**2 + 5 * x + 12 * y + 22


# der func
def der(x, y):
    return np.array([2 * x + 5, 4 * y + 12])


if __name__ == "__main__":
    # grid values
    xAxis = np.arange(-12.5, 7.5, 0.1)
    yAxis = np.arange(-13, 7, 0.1)
    x, y = np.meshgrid(xAxis, yAxis)
    z = obj(x, y)

    # create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    surface = ax.plot_surface(x, y, z, cmap="ocean", alpha=0.5)

    ax.set_title("3D Surface Plot of the Objective Function")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis (Function Value)")

    plt.show()
