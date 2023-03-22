import matplotlib.pyplot as plt
import numpy as np

# generate data
data = np.random.normal(size=(100, 4))

# plot the data
plt.boxplot(data)

# set the labels of the x and y axis
plt.xticks([1, 2, 3, 4], ['A', 'B', 'C', 'D'])
plt.ylabel('Value')

# add a title
plt.title('Box Plot')

# show the plot
plt.show()
