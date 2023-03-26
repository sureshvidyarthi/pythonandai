import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y)
img = plt.imread('meta/images.jpg')
plt.imshow(img)