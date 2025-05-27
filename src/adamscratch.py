# this code is import from plotview file
import numpy as np
import matplotlib.pyplot as plt
from plotview import obj, der


# adam optimizer
def adam(obj, der):
    n_iter = 10000
    alpha = 0.01
    beta1 = 0.9
    beta2 = 0.999
    eps = 1e-8
    bounds = np.array([[-12.5, 7.5], [-13, 7.0]])

    # initial point
    x = np.array([-12.5, -13])
    scores = []
    trajectory = []

    # initialize adam
    m = np.zeros(bounds.shape[0])
    v = np.zeros(bounds.shape[0])

    # adam formula
    for t in range(n_iter):
        g = der(x[0], x[1])
        for i in range(x.shape[0]):
            m[i] = beta1 * m[i] + (1.0 - beta1) * g[i]
            v[i] = beta2 * v[i] + (1.0 - beta2) * g[i] ** 2
            mhat = m[i] / (1.0 - beta1 ** (t + 1))
            vhat = v[i] / (1.0 - beta2 ** (t + 1))
            x[i] -= alpha * mhat / (np.sqrt(vhat) + eps)

        score = obj(x[0], x[1])
        scores.append(score)
        trajectory.append(x.copy())

    return x, scores, trajectory, bounds


# run optimizer
best, scores, trajectory, bounds = adam(obj, der)

# plotting
x = np.arange(bounds[0, 0], bounds[0, 1], 0.01)
y = np.arange(bounds[1, 0], bounds[1, 1], 0.01)
X, Y = np.meshgrid(x, y)
Z = obj(X, Y)

# best values
bestScore = obj(best[0], best[1])
print("Best: ", best)
print("Best score: ", f"{bestScore:.2f}")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="ocean", alpha=0.5)
ax.scatter(best[0], best[1], obj(best[0], best[1]), color="blue", label="best")
ax.plot(
    [point[0] for point in trajectory],
    [point[1] for point in trajectory],
    scores,
    color="green",
    label="Trajectory",
)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Objective")
ax.legend()
plt.show()
