# flake8: noqa
date, temperature = np.loadtxt('./data/munich_temperatures_average.txt', unpack=True)
plt.plot(date, temperature, '.')
plt.ylim([-20, 30])

def f(t, a, b, c):
    return a * np.cos(2*np.pi * t + b) + c

popt, pcov = optimize.curve_fit(f, date, temperature)

plt.plot(date, f(date, *popt), c='red')
np.sqrt(np.diag(pcov)), popt
