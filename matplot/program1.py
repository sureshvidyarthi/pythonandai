import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,4,5,9,7])
y = np.array([3, 3,3,6,8])

# plt.plot(x,y) // simple grapgh
# plt.plot(x,y, marker='o') // marker
# plt.plot(x,y, linestyle= 'dotted') // linestyle
# plt.plot(x,y, color= 'hotpink') // color
plt.plot(x,y, linewidth='3')
plt.show()