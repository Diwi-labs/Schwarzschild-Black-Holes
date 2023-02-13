import numpy as np
import rk4l
import matplotlib.pyplot as plt

b = 4/27

def ic(u, t):
    return -(np.sqrt( (1/b)**2 + (u)**2 - (u)**3))

def u(u, t):
    return 1.5*(u)**2 - u

def condition(u, t):
    if 1/u >= 1.01:
        return False
    else:
        return True



#extrapolate(U, U0, t, tn, condition)


