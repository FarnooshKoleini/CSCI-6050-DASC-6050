import nibabel as nib
import numpy as np 
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import asarray
from scipy import ndimage, misc, stats
import cv2


### Load the image 

img  = nib.load('/Users/koleinif20/Desktop/CVprojects/goldendoggray.jpg')
img_data = img.get_fdata()
imgs = img_data[:, :, 23]

rows, col = imgs.shape
my_nlist = [[] for k in range(y.shape[0])]
print(im_arr[2,2])
for i in range(0, rows):
    for j in range(0, col): 
        pixel = imgs[i, j]
        for k in range(y.shape[0]):
            if pixel == [k]:               
                my_nlist[k].append(pixel) 