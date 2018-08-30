import cv2

print("OpenCV Python Tutorial using version " + cv2.__version__)

img = cv2.imread("img.pgm",cv2.IMREAD_GRAYSCALE)

cv2.imshow('casablanca',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("casablanca",cv2.WINDOW_NORMAL)
cv2.imshow('casablanca',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img.png",img)
