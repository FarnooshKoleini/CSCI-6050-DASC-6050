import matplotlib.pyplot as plt
import cv2 as cv # You won't be needing cv2, it is just needed to create this example

img = cv.imread('/Users/koleinif20/Desktop/CVprojects/goldendog.jpeg', 0) # notice the grayscale 
# hist contains the list of pixels with the same intensity for each intensity in the picture
plt.hist(img)
plt.xlabel('Intensities contained in the image')
plt.ylabel('Amount of pixels found for each intensity')
plt.show() # in case you want to visualize it