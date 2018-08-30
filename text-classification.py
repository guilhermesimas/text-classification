import cv2
from matplotlib import pyplot as plt

print("OpenCV Python Tutorial using version " + cv2.__version__)

img = cv2.imread('img.pgm',0)
cv2.imshow('casablanca',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    exit()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('img.png',img)
    cv2.destroyAllWindows()
    exit()

plt.imshow(img, cmap = "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])
plt.show()
