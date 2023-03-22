# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y, color='green')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y, marker='o')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y, linestyle='dashed')
# plt.show()




import matplotlib.pyplot as plt
import numpy as np

# generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# plot the data
plt.plot(x, y)

# set the limits of the x and y axis
plt.xlim(0, 10)
plt.ylim(-1.2, 1.2)

# set the ticks of the x and y axis
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(-1, 1.1, 0.5))

# set the labels of the x and y axis
plt.xlabel('x')
plt.ylabel('sin(x)')

# add a title
plt.title('Sine Function')

# add a legend
plt.legend(['sin(x)'])

# add a grid
plt.grid()

# show the plot
plt.show()



