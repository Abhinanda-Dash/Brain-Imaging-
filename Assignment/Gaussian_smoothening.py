#import important libraries
import matplotlib.pyplot as plt
from scipy import misc, ndimage

brain = plt.imread("Brain.jpg") #File is read as an array in python
brain.shape #Gives dimensions of the file
plt.imshow(brain, cmap='Greys_r') #Allows the image to be drawn in greyscale
plt.show() #Allows the drawn image to be displayed 
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Representing the image array as a histogram
plt.hist(brain, bins = 10) #Constructs A histogram based on the image array and the number of bins.
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Begin performing Gaussian Smoothening
one_blurred = ndimage.gaussian_filter(brain, sigma=5) #Image is passed through Gaussian filter with sigma = 5
least_blurred.shape #Dimensions of the smoothened image
plt.imshow(least_blurred, cmap='Greys_r') #Smoothened image is drawn by the program
plt.show() #Drawn image is displayed
#Save the image
#Close the file

plt.hist(least_blurred, bins=10) #Construct the histogram for the smoothened image
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Gaussian Smoothening when Sigma = 10
two_blurred = ndimage.gaussian_filter(brain, sigma=10) #Image is passed through Gaussian filter with sigma = 10
less_blurred.shape #Obtain dimensions of smoothened image
plt.imshow(less_blurred, cmap='Greys_r') #Smoothened image is drawn by the program
plt.show() #Drawn image is displayed
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

plt.hist(less_blurred, bins = 10) #Construct the histogram for the smoothened image
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Gaussian Smoothening when sigma = 20
three_blurred = ndimage.gaussian_filter(brain, sigma=20) #Image is passed through Gaussian filter with sigma = 20
three_blurred.shape #Obtain dimensions of smoothened image
plt.imshow(three_blurred, cmap='Greys_r') #Smoothened image is drawn by the program
plt.show() #Drawn image is displayed
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.
plt.hist(three_blurred, bins = 10) #Construct the histogram for the smoothened image
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Gaussian Smoothening when sigma = 30
four_blurred = ndimage.gaussian_filter(brain, sigma=30) #Image is passed through Gaussian filter with sigma = 30
four_blurred.shape #Obtain dimensions of smoothened image
plt.imshow(four_blurred, cmap='Greys_r') #Smoothened image is drawn by the program
plt.show() #Drawn image is displayed
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.
plt.hist(four_blurred, bins = 10) #Construct the histogram for the smoothened image
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Gaussian Smoothening when sigma = 40
five_blurred = ndimage.gaussian_filter(brain, sigma=40) #Image is passed through Gaussian filter with sigma = 40
five_blurred.shape #Obtain dimensions of smoothened image
plt.imshow(five_blurred, cmap='Greys_r') #Smoothened image is drawn by the program
plt.show() #Drawn image is displayed
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

plt.hist(five_blurred, bins = 10) #Construct the histogram for the smoothened image
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

#Gaussian Smoothening when sigma = 50
six_blurred = ndimage.gaussian_filter(brain, sigma=50) #Image is passed through Gaussian filter with sigma = 50
six_blurred.shape #Obtain dimensions of smoothened image
plt.imshow(six_blurred, cmap='Greys_r') #Smoothened image is drawn by the program
plt.show() #Drawn image is displayed
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.

plt.hist(six_blurred, bins = 10) #Construct the histogram for the smoothened image
plt.show() #Display the histogram
#Manually save the image as a .png file.
#Manually close the image in order to execute the rest of the commands.
