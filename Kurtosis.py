import cv2
from scipy.stats import kurtosis, skew
img1 = '/Users/koleinif20/Desktop/CVprojects/vlg.jpg'
gray_img = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
print(kurtosis(gray_img,axis =None))
print(skew(gray_img,axis =None))