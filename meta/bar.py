import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.arange(4)
y = [10, 20, 15, 25]

# plot the data
plt.bar(x, y)

# set the labels of the x and y axis
plt.xticks(x, ['A', 'B', 'C', 'D'])
plt.ylabel('Value')

# add a title
plt.title('Bar Chart')

# show the plot
plt.show()
