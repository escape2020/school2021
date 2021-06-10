# 1
A = np.random.uniform(0, 1, size=(10, 10))

#2 
A_sym = A + A.T
plt.matshow(A_sym)
plt.grid()

#3 
values, vectors = linalg.eigh(A_sym)