## use Python Imaging Library (PIL) Module to Change Contrast of an Image. 
# require Image and ImageEnhance Classes from PIL module 
# in order to Change the Contrast of an Image in Python.
# Image class is used to perform some basic Operations on Images like Opening, Saving, Closing etc.
# ImageEnhance Class is used to enhance the Properties of an Image like Brightness,Contrast, Color etc. 

from PIL import Image,ImageEnhance
import numpy as np

# import the original image
img=Image.open("/Users/koleinif20/Desktop/CVprojects/goldendog.jpeg")

# create an object for ImageEnhance.Contrast Class in order to change the Contrast 
img_contr_obj=ImageEnhance.Contrast(img)

# factor is a floating-point number which enhances the Contrast of an Image.
# factor can have several values. Hence, they can be written as follows
# if factor > 1 Increases Contrast according to the given factor Values
# if factor < 1 Decreases Contrast according to the given factor Values
# and if the value of factor is 1 (i.e. factor=1) then the Contrast of the Image remains Same.
#.2 = very low, .5 = low, 1 = medium, 3 = high, 10 = very high
 
factor = [0.2, 0.5, 1, 3, 10] 
par = np.array(factor)

# creating images with different contrasts, parameters

for i in par: 
    e_img=img_contr_obj.enhance(i)
    e_img.show()   # the Enhanced Image can be Viewed.  



