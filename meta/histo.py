import matplotlib.pyplot as plt
import numpy as np

# generate data
data = np.random.normal(size=1000)

# plot the data
plt.hist(data, bins=20)

# set the labels of the x and y axis
plt.xlabel('Value')
plt.ylabel('Frequency')

# add a title
plt.title('Histogram')

# show the plot
plt.show()
