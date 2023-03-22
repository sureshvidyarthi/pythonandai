import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# plot the data
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

# add a legend
plt.legend()

# show the plot
plt.show()
