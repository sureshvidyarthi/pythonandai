import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)

# Set the x and y limits
plt.xlim(0, 10)
plt.ylim(-1, 1)

# Set the x and y ticks
plt.xticks(np.arange(0, 11, 2))
plt.yticks([-1, 0, 1])

# Set the legend
plt.legend(['sine'])

# Set the labels for the x and y axes and the title
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')

# Show the plot
plt.show()
