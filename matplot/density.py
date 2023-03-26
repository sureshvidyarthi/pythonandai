import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size=100)
y = np.random.normal(size=100)
plt.scatter(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.grid()
plt.show()
# plt.savefig('image.jpg')
plt.close()
plt.clf()
