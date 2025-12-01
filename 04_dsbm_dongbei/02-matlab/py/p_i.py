import numpy as np

n = int(input('n: '))
x = np.arange(1, 2*n, 2)
y = (-1) ** np.arange(2, n+2) / x
p = np.sum(y) * 4

print(p)
