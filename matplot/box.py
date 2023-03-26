import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(size=(100, 5))
plt.boxplot(data, labels=['A', 'B', 'C', 'D', 'E'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot')
plt.grid()
plt.show()
