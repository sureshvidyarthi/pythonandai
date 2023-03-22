import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.arange(4)
y1 = [10, 20, 15, 25]
y2 = [5, 15, 10, 20]

# plot the data
plt.bar(x, y1, label='Group 1')
plt.bar(x, y2, bottom=y1, label='Group 2')

# set the labels of the x and y axis
plt.xticks(x, ['A', 'B', 'C', 'D'])
plt.ylabel('Value')

# add a title
plt.title('Stacked Bar Chart')

# add a legend
plt.legend()

# show the plot
plt.show()
