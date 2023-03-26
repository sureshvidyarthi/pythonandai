import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.plot(x, y1, label='Sine')
plt.plot(x, y2, label='Cosine')

# Set the x and y limits
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Set the x and y ticks
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(-1, 2, 1))

# Add a legend
plt.legend(loc='upper right')

# Add axis labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Functions')

# Display the plot
plt.show()
