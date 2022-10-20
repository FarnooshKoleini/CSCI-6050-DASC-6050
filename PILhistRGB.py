# from PIL import Image
# import cv2  
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv2.imread('/Users/koleinif20/Desktop/CVprojects/goldendoggray.jpg')
# histg = cv2.calcHist([img], [0], None, [256], [0 , 256])
# plt.plot(histg)
# plt.show()
# par = np.array(histg)
# print(par)
# total = np.sum(par)
# prob = par/total
# print(np.sum(prob))
# mean = np.mean(img)
# var = np.var(img)

from PIL import Image
import cv2  
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('/Users/koleinif20/Desktop/CVprojects/goldendoggray.jpg')
histg = cv2.calcHist([img], [1], None, [256], [0 , 256])
plt.plot(histg)
plt.xlabel('Intensity')
plt.ylabel('Number of pixels')
plt.title('Probablity distribution for color image, blue channel')
plt.show()
# par_blue = np.array(histg)
# total_blue = np.sum(par_blue)
# prob_blue = par_blue/total_blue
# print('Sum of the probabilities for different intesities color image, blue channel:',np.sum(prob_blue))

# from PIL import Image
# import cv2  
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv2.imread('/Users/koleinif20/Desktop/CVprojects/goldendoggray.jpg')
# histg = cv2.calcHist([img], [1], None, [256], [0 , 256])
# plt.plot(histg)
# plt.xlabel('Intensity')
# plt.ylabel('Number of pixels')
# plt.title('Probablity distribution for color image, green channel')
# plt.show()
# par_blue = np.array(histg)
# total_blue = np.sum(par_blue)
# prob_blue = par_blue/total_blue
# print('Sum of the probabilities for different intesities color image, green channel:',np.sum(prob_blue))




#data = img2.getdata()

# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
#r = [(d[0], 0, 0) for d in data]
#g = [(0, d[1], 0) for d in data]
#b = [(0, 0, d[2]) for d in data]

#print(np.sum(r))
#print(np.sum(g))
#print(np.sum(b))






