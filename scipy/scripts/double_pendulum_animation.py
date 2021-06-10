from scipy.constants import g
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib import animation


L = 0.5
m = 0.1

t_start = 0
t_end = 20
fps = 50
frames = (t_end - t_start) * fps


def pendulum_model(t, y):
    """
    The right-hand side of the pendulum ODE
    """
    phi_1, phi_2, p_1, p_4 = y

    c = (m * L**2)
    cos_delta_phi = np.cos(phi_1 - phi_2)
    sin_delta_phi = np.sin(phi_1 - phi_2)
    denominator = 16 - 9 * cos_delta_phi**2

    dphi_1 = 6 / c * (2 * p_1 - 3 * cos_delta_phi * p_4) / denominator
    dphi_2 = 6 / c * (8 * p_4 - 3 * cos_delta_phi * p_1) / denominator

    dp_1 = -c / 2 * ( dphi_1 * dphi_2 * sin_delta_phi + 3 * g / L * np.sin(phi_1))
    dp_4 = -c / 2 * (-dphi_1 * dphi_2 * sin_delta_phi + g / L * np.sin(phi_2))

    return [dphi_1, dphi_2, dp_1, dp_4]


# initial values
y0 = [np.pi / 3, -np.pi / 4, 0, 0.065]


solution = solve_ivp(
    pendulum_model,
    (t_start, t_end),
    y0,
    t_eval=np.linspace(t_start, t_end, frames),
)

x1s = + L * np.sin(solution.y[0])
y1s = - L * np.cos(solution.y[0])

x2s = x1s + L * np.sin(solution.y[1])
y2s = y1s - L * np.cos(solution.y[1])

plt.plot(x1s, y1s, '-', color='xkcd:sky blue')
plt.plot(x2s, y2s, '-', color='xkcd:dark magenta')

fig, ax = plt.subplots(figsize=(6, 5))

ax.set_ylim([-1.1, 0.2])
ax.set_xlim([1, -1])

pendulum1, = ax.plot([], [], '-', alpha=0.5, color='xkcd:sky blue')
pendulum2, = ax.plot([], [], '-', alpha=0.5, color='xkcd:dark magenta')

def init():
    pendulum1.set_data([], [])
    pendulum2.set_data([], [])
    return (pendulum1, pendulum2)

def update(n):
    # update the line data
    pendulum1.set_data([0, x1s[n]], [0, y1s[n]])
    pendulum2.set_data([x1s[n], x2s[n]], [y1s[n], y2s[n]])
    return (pendulum1, pendulum2)


anim = animation.FuncAnimation(fig, update, init_func=init, frames=frames, blit=True, interval=1000 / fps)
anim.save('animation_pendulum.mp4', writer="ffmpeg")