import numpy as np
import matplotlib.pyplot as plt

# Creating a function which takes in a 2nd order ODE with initial conditions and returns first and 2nd order approximate solutions
# We will be given a 2nd order equation which we will use RK4 to solve for the 1st order
# We then use eulers method to approximate the position
# Return a vector with the 2nd, 1st

V = [ 2, 1]
path = [1]

def rk4(U, y0, tn):
    k1 = U(y0)
    k2 = U(y0 + k1 * tn / 2)
    k3 = U(y0 + k2 * tn / 2)
    k4 = U(y0 + k3 * tn)

    return y0 + (k1 + 2 * k2 + 2 * k3 + k4) * (tn / 6)

def Euler(V, tn):
    return V[1] + tn*V[0]


def acc(y):
    return 4*y

def con(y):
    if y < np.exp(2):
        return True
    else:
        return False

while con(V[-1]):
    V[0] = rk4(acc, V[0], 0.000001)
    V[1] = Euler(V, 0.000001)
    path.append(V[-1])


print(len(path))
k = [1, path[65577], path[65577*2], path[65577*3], path[65577*4], path[65577*5], path[65577*6], path[65577*7], path[65577*8], path[65577*9], path[-1]]
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
y = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
plt.plot(x , k)
plt.plot(x, np.exp(y))
plt.show()




