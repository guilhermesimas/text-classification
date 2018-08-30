import cv2
import numpy as np

img = cv2.imread("img.pgm")

print(img[50,50])
print(img.shape)
print(img.size)
print(img.dtype)

width,height,_ = img.shape

img_partial = img[int(width*1/4):int(width*3/4),int(height*1/4):int(height*3/4)]

cv2.imshow("partial image",img_partial)
cv2.waitKey(0)
