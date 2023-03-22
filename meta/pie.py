import matplotlib.pyplot as plt
import numpy as np

# generate data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# plot the data
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# add a title
plt.title('Pie Chart')

# show the plot
plt.show()
