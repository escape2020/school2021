import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import rainbow
import numpy as np
from scipy.integrate import odeint
from scipy.io import loadmat

import pysindy as ps

# Generate training data
# for the  [Krogdahl equation](https://en.wikipedia.org/wiki/List_of_nonlinear_ordinary_differential_equations)
# for [stellar pulsations](https://en.wikipedia.org/wiki/Stellar_pulsation)

# Equation parameters
mu = 1.2
lam = 1.5


def f(q, t):
    return [
        q[1],
        -1 * q[0]
        + (2 / 3) * lam * q[0] ** 2
        - (14 / 27) * (lam ** 2) * q[0] ** 3
        + mu * (1 - q[0] ** 2) * q[1]
        + (2 / 3) * lam * (1 - lam * q[0]) * (q[1] ** 2),
    ]


dt = 0.01
t_train = np.arange(0, 25, dt)
q0_train = [2, 0]
q_train = odeint(f, q0_train, t_train)
# Fit the model

poly_order = 5
threshold = 0.01

model = ps.SINDy(
    optimizer=ps.STLSQ(threshold=threshold),
    feature_library=ps.PolynomialLibrary(degree=poly_order),
)
model.fit(q_train, t=dt)
model.print()
print("Expected equation\n")
print("x0' = x1\n")
print(
    "x1' = -1 * x0 + %f * x0 ** 2 - %f * x0 ** 3 + %f * x1  - %f * (x0 ** 2) * x1 + %f *  x1 ** 2  - %f * x0 * x1 ** 2"
    % (
        (2.0 / 3.0) * lam,
        (14.0 / 27.0) * (lam ** 2),
        mu,
        mu,
        (2 / 3) * lam,
        (2 / 3) * (lam ** 2),
    )
)

# Simulate and plot the results

q_sim = model.simulate(q0_train, t_train)
plot_kws = dict(linewidth=2.5)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(t_train, q_train[:, 0], "r", label="$q_0$", **plot_kws)
axs[0].plot(t_train, q_train[:, 1], "b", label="$q_1$", alpha=0.4, **plot_kws)
axs[0].plot(t_train, q_sim[:, 0], "k--", label="model", **plot_kws)
axs[0].plot(t_train, q_sim[:, 1], "k--")
axs[0].legend()
axs[0].set(xlabel="t", ylabel="$q_k$")

axs[1].plot(q_train[:, 0], q_train[:, 1], "r", label="$q_k$", **plot_kws)
axs[1].plot(q_sim[:, 0], q_sim[:, 1], "k--", label="model", **plot_kws)
axs[1].legend()
axs[1].set(xlabel="$q_1$", ylabel="$q_2$")
fig.savefig("sindy_krogdhal.svg")
# The library supports cross validation, read more in the documentation at
# https://pysindy.readthedocs.io/en/latest/examples/4_scikit_learn_compatibility.html
