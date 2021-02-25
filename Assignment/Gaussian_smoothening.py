import matplotlib.pyplot as plt
from scipy import misc, ndimage
brain = plt.imread("Brain.jpg")
brain.shape
plt.imshow(brain, cmap='Greys_r')
plt.show()
plt.hist(brain, bins = 10)
plt.show()
least_blurred = ndimage.gaussian_filter(brain, sigma=5)
plt.imshow(least_blurred)
plt.show()
plt.hist(least_blurred, bins=10)
plt.show()
