import cv2 
import numpy as np
img = cv2.imread('/Users/koleinif20/Desktop/CVprojects/vhc.jpg')
mean = np.mean(img)
print('Mean:',mean)
var = np.var(img)
print('Variance:',var)