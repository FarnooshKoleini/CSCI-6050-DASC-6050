# Farnoosh Koleini
# 30 Nov, 2022

# CSCI 4150/ CSCI 6050/ DASC 6050: Programming As- signment 01
# Image Forensics

# Goal: The overarching goal of this assignment is to determine if an image is tam-
# pered using Benford’s law.

## First Step:

# Select five to six natural images of the same spatial and intensity reso- lution.
# For example, 1024 × 1024 spatial resolutions with 8-bit intensity resolution. 
# This is your image dataset.

# What is a natural image? 
# Natural image analysis often refers to problems such as object detection, face recognition
# and 3D reconstruction, using images from normal RGB cameras.

# Import the Images module from pillow
from PIL import Image

# Open the image by specifying the image path.
image_path1 = "blue flower.jpeg"
image_file1 = Image.open(image_path1)
image_path2 = "colorfulflower.jpeg"
image_file2 = Image.open(image_path2)
image_path3 = "pinkflower.jpeg"
image_file3 = Image.open(image_path3)
image_path4 = "purpleflower.jpeg"
image_file4 = Image.open(image_path4)
image_path5 = "redflower.jpeg"
image_file5 = Image.open(image_path5)


# Changing the image resolution using quality parameter
# Example-1
image_file1.save("P1.jpeg", quality=85)
image_file2.save("P2.jpeg", quality=85)
image_file3.save("P3.jpeg", quality=85)
image_file4.save("P4.jpeg", quality=85)
image_file5.save("P5.jpeg", quality=85)

# Computing DCT and checking benford's law for both 
# the original image and the tampered one

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
from PIL import Image, ImageFilter

def firstDigit(number):
    digits = (int)(math.log10(number)) 
    number = (int)(number / pow(10, digits)) 
    return number

def graph(image_name,flag):
    
    img = cv2.imread(image_name,0)
    norm_img = np.zeros((800,800))
    final_img = cv2.normalize(img,  norm_img, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite('city_normalized.jpeg', final_img)
    img = cv2.imread('./city_normalized.jpeg',0)
    imf = np.float32(img)/255.0
    dst = cv2.dct(imf)
    img = np.uint8(dst)*255.0
    
    col = dst.reshape(dst.shape[0]*dst.shape[1],).tolist()
    length = len(col)
    
    
    dict_freq = {}
    for digit in range(1,10):
        dict_freq[str(digit)] = 0

    for value in col:
        if (type(value) is int or type(value) is float) and value>0:
    #         print(value)
            f_digit = firstDigit(value*1000000000000000000000000)
            dict_freq[str(f_digit)]+=1

    benford_dict = {}
    for digit in range(1,10):
        benford_dict[str(digit)] = math.log10(1+1/digit)
    freq_benf = np.array(list(benford_dict.values()))
    total_entries = 0
    for i in list(dict_freq.values()):
        total_entries+=i
    digits = list(dict_freq.keys())
    
    digits = list(dict_freq.keys())
    frequency = list(dict_freq.values())

    benford_freq = freq_benf * total_entries

    plt.bar(range(len(dict_freq)),frequency,tick_label=digits,color = 'silver')
    if flag==0:
        plt.plot(digits,frequency,label="Original Image Analysis",color='black',linestyle='dashed',linewidth=3,marker='o')
    else:
        plt.plot(digits,frequency,label="Modified Image Analysis",color='black',linestyle='dashed',linewidth=3,marker='o')
    plt.plot(digits,benford_freq,label="Actual Benford's Analysis",color='blue',linestyle='dashed',linewidth=3,marker='*')
    plt.xlabel('Digits')
    plt.ylabel('Frequency')
    plt.legend(loc='best')
    plt.savefig('result.png', dpi=300, bbox_inches='tight')
    plt.show()


# Checking benford's law for both original images and tampered (gussian bluring) ones

OriImage = Image.open('./P1.jpeg')
blurImage = OriImage.filter(ImageFilter.GaussianBlur(5)) # tampering an image
blurImage.save("blurImageP1.jpeg") #saving a tamper image
graph('./P1.jpeg',0)
graph('./blurImageP1.jpeg',0)

OriImage = Image.open('./P2.jpeg')
blurImage = OriImage.filter(ImageFilter.GaussianBlur(5))
blurImage.save("blurImageP2.jpeg")
graph('./P2.jpeg',0)
graph('./blurImageP2.jpeg',0)

OriImage = Image.open('./P3.jpeg')
blurImage = OriImage.filter(ImageFilter.GaussianBlur(5))
blurImage.save("blurImageP3.jpeg")
graph('./P3.jpeg',0)
graph('./blurImageP3.jpeg',0)

OriImage = Image.open('./P4.jpeg')
blurImage = OriImage.filter(ImageFilter.GaussianBlur(5))
blurImage.save("blurImageP4.jpeg")
graph('./P4.jpeg',0)
graph('./blurImageP4.jpeg',0)

OriImage = Image.open('./P5.jpeg')
blurImage = OriImage.filter(ImageFilter.GaussianBlur(5))
blurImage.save("blurImageP5.jpeg")
graph('./P5.jpeg',0)
graph('./blurImageP5.jpeg',0)



