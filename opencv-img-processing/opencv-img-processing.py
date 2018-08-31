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

img_color = cv2.imread("color.tiff")
cv2.imshow("Peppers",img_color)
cv2.waitKey(0)

b, g, r = cv2.split(img_color)
b.fill(0)
g.fill(0)

cv2.imshow("Red",cv2.merge((b,g,r)))
cv2.waitKey(0)

cv2.imshow("Green channel",img_color[:,:,1])
cv2.waitKey(0)

img_color[:,:,1] = 0
img_color[:,:,2] = 0
cv2.imshow("Blue",img_color)
cv2.waitKey(0)

img_color = cv2.imread("color.tiff")
img_ruler = cv2.imread("ruler.tiff")

cv2.imshow("Peppers",img_color)
cv2.imshow("Ruler",img_ruler)
cv2.waitKey(0)

img_merged = cv2.addWeighted(img_color,0.5,img_ruler,0.5,0)
cv2.imshow("Peppers with Ruler",img_merged)
cv2.waitKey(0)
