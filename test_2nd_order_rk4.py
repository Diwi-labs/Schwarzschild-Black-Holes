import numpy as np

#attempting to model x^3

dderiv = []
derive = []

def function_to_model(x, t):
    return 6*x

def fdash(x, t):
    return dderiv[-1]

domain = np.array(0, 5, 0.001)


for i in domain:

