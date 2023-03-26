import matplotlib.pyplot as plt
import numpy as np
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 30, 40, 50]
plt.bar(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.grid()
plt.show()
