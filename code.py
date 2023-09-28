import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("inputimage.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img)
plt.show()

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.axis('off')
plt.imshow(gray_img)
plt.show()


#inv_gray_img = 255 - gray_img
inv_gray_img = cv2.bitwise_not(gray_img)
plt.axis('off')
plt.imshow(inv_gray_img)
plt.show()


blur_img = cv2.GaussianBlur(inv_gray_img,(21,21),0)
plt.axis('off')
plt.imshow(blur_img)
plt.show()

#inv_blur_img = 255 - blur_img
inv_blur_img = cv2.bitwise_not(blur_img)
plt.axis('off')
plt.imshow(inv_blur_img)
plt.show()


pencil_img = cv2.divide(gray_img,inv_blur_img,scale = 256.0)
plt.axis('off')
plt.imshow(pencil_img)
plt.show()


cv2.imwrite("./output_image.png",pencil_img)