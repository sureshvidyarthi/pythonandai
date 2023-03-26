import matplotlib.pyplot as plt
import numpy as np

x = ['A', 'B', 'C', 'D', 'E']
y1 = [10, 20, 30, 40, 50]
y2 = [5, 10, 15, 20, 25]
plt.bar(x, y1, label='Group 1')
plt.bar(x, y2, bottom=y1, label='Group 2')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Plot')
plt.legend()
plt.grid()
plt.show()
