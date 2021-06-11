# flake8: noqa
# fixed model parameters
B = 0.1 # birth rate
delta = 0.0001 # rate of natural casues of death
beta = 0.00016 # transmission coefficent
gamma = 0.0001 # resurrection rate
alpha = 0.0001 # rate of destroyed zombies
rho = 0.01 # rate of cured zombies

# initial conditions
S0 = 5000.              # initial population
Z0 = 0                 # initial zombie population
R0 = 0                 # initial dead population
y0 = [S0, Z0, R0]     # initial condition vector

def f_model(t, y):
    Si = y[0]
    Zi = y[1]
    Ri = y[2]
    # the model equations (see Munz et al. 2009)
    f0 = B - beta*Si*Zi - delta*Si + rho*Zi # additional cured zombies
    f1 = beta*Si*Zi + gamma*Ri - alpha*Si*Zi - rho*Zi # subtract cured zombies
    f2 = delta*Si + alpha*Si*Zi - gamma*Ri
    return [f0, f1, f2]


t_start, t_end = 0, 150  # 200 days of zobie acopalypse
solution = solve_ivp(f_model, (t_start, t_end), y0, t_eval=np.linspace(t_start, t_end, 200))

s = solution.y[0, :]
z = solution.y[1, :]
plt.plot(solution.t, s, label='survivors')
plt.plot(solution.t, z, label='zombies')
plt.xlabel('t / days')
plt.ylabel('Population')
plt.legend()