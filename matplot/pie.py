import matplotlib.pyplot as plt
import numpy as np
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [10, 20, 30, 40, 50]
plt.pie(sizes, labels=labels)
plt.title('Pie Chart')
plt.show()
