# some code to create a nice animation within the notebook.
#this takes a couple of minutes on my machine so I commented it out
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from functools import partial
from tqdm import tqdm
from scipy import special

# fix the radius of the drum
DRUM_RADIUS = 1

def drumhead_height(n, k, radius, theta, t):
    '''Solution to the Drumhead problem with a fixed membrane on the edge of the drum
    See https://en.wikipedia.org/wiki/Vibrations_of_a_circular_membrane
    '''
    kth_zero = special.jn_zeros(n, k)[-1] # fix the drum on the outter edge to be zero.
    return np.cos(t) * np.cos(n * theta) * special.jn(n, radius * kth_zero / DRUM_RADIUS)


# create two coordinate vectors containing all combinations of radius and theta we want to plot
r = np.linspace(0, DRUM_RADIUS, 50)
t = np.linspace(0, 2 * np.pi, 50)
radius, theta = np.meshgrid(r, t) # this creates all combinations we are interested in

x = radius * np.cos(theta)
y = radius * np.sin(theta)

my_drum = partial(drumhead_height, n=2, k=1, radius=radius, theta=theta)

frames = 200
fps = 25

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, my_drum(t=0), cmap='YlGnBu')

bar = tqdm(total=frames)

def update(i):
    bar.update()
    t = i / fps
    ax.cla()
    z = my_drum(t=t)
    ax.plot_surface(x, y, z, cmap='YlGnBu', vmin=-0.5, vmax=0.5)
    ax.set_zlim(-0.5, 0.5)
   
ani = FuncAnimation(fig, update, frames=frames, interval=1000 / fps, blit=False, repeat=False)
ani.save('animation_membrane.mp4', writer="ffmpeg")