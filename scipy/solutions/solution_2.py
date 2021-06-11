# flake8: noqa
a, b = .8, .4
epsilon = np.sqrt(1 - b**2/a**2)

t = np.linspace(0, 2*np.pi, 100)
plt.plot(a*np.cos(t), b*np.sin(t))
plt.xlim([-1, 1])
plt.ylim([-0.5, 0.5])
plt.gca().set_aspect(1)
plt.text(-0.2, 0, f'Ellipse with eccentrictiy: {epsilon:.4}')

circumference = 4 * a * special.ellipe(epsilon**2)

f = lambda t: 4*a* np.sqrt(1 - epsilon**2 * np.sin(t)**2)
val, abserr = quad(f, 0, np.pi/2)

print(f'numerical solution= {val}, {abserr}')
print(f'analytical solution= {circumference}')
