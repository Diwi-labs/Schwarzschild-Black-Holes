import numpy as np
import rk4plus1

derive = [0.03]
values = [0.1]

def fddash(x, t):
    return 2

def fdash(x, t):
    return 3*(x**2)

domain = np.arange(0.1, 3, 0.000001)

for i in domain:
    derive.append(rk4plus1.run(fddash, i, derive[-1], 0.000001))
    values.append(rk4plus1.run(fdash, i, values[-1], 0.000001))


print(values[-1])
print(derive[0:10])




