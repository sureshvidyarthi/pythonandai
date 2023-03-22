import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and subplot
fig, ax = plt.subplots()

# Plot the data on the subplot
ax.plot(x, y)

# Customize the plot
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Sine Wave')

# Show the plot on screen
plt.show()
