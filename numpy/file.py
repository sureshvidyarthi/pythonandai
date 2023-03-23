import numpy as np

# create an array of integers
numbers = np.array([1, 2, 3, 4, 5])

# write the array to a text file using the 'savetxt' method
np.savetxt('file.txt', numbers)

# read the array from the text file using the 'loadtxt' method
numbers_from_file = np.loadtxt('file.txt')

print(numbers_from_file)
