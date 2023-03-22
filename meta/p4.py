import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# plot the data
plt.plot(x, y)

# annotate the plot with text
plt.text(2, 1, 'Maximum Value')

# show the plot
plt.show()
