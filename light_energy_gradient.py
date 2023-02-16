import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

def f(x):
    return (1 - 1/x)


colours = ["#A8453A",  "#A8453A", "#A8453A", "#A8453A", "#A8453A", "#A8453A", "#A8453A", "#A8453A", "#A8453A","#A8453A",  "#CD6C61",  "#CD6C61", "#CD6C61", "#CD6C61", "#CD6C61", "#CD6C61", "#CD6C61", "#CD6C61", "#CD6C61","#CD6C61",  "#E39087",  "#E39087", "#E39087", "#E39087", "#E39087", "#E39087", "#E39087", "#E39087", "#E39087","#E39087",  "#F0AAA3",  "#F0AAA3", "#F0AAA3", "#F0AAA3", "#F0AAA3", "#F0AAA3", "#F0AAA3", "#F0AAA3", "#F0AAA3","#F0AAA3",  "#F5BDB7",  "#F5BDB7", "#F5BDB7", "#F5BDB7", "#F5BDB7", "#F5BDB7", "#F5BDB7", "#F5BDB7", "#F5BDB7","#F5BDB7", ]
print(len(colours))

x = np.linspace(1, 20, 50)
y = f(x)



plt.scatter(x, y, c=colours )
plt.title("Percentage of energy remaining given stating position of photon")
plt.xlabel("Starting radius in units of 1 Schwarschild Radius")
plt.ylabel("Scaled Energy remaining")
plt.show()