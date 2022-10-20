from PIL import Image,ImageEnhance
img=Image.open("/Users/koleinif20/Desktop/CVprojects/goldendog.jpeg")
img_contr_obj=ImageEnhance.Color(img)
factor = 0.01
e_img=img_contr_obj.enhance(factor)
e_img.show()


