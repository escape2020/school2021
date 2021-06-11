# flake8: noqa
from scipy import stats
# 1
t = np.linspace(-30, 30, 100)
sigma = 10 / np.sqrt(2)
A = np.random.normal(0, sigma, size=(50, 50))
A = (A + (A.T))

# 2
f, [ax1, ax2] = plt.subplots(1, 2)
ax1.imshow(A)
ax1.grid()

ax2.hist(A.ravel(), bins=35, density=True)
ax2.plot(t, stats.norm.pdf(t, loc=A.mean(), scale=A.std()), color='crimson')


# 3
t = np.linspace(0, 1500, 500)
A_chi = A**2 + A**2

# 4
f, [ax1, ax2] = plt.subplots(1, 2)
ax1.imshow(A_chi)
ax1.grid()

k, loc, scale  = stats.chi2.fit(A_chi)

ax2.hist(A_chi.ravel(), bins=60, density=True)
ax2.plot(t, stats.chi2.pdf(t, df=k, loc=loc, scale=scale), color='crimson')
ax2.set_xlim([0, 1000])
None
