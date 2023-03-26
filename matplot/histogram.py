import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(size=1000)
plt.hist(data, bins=30)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid()
plt.show()
