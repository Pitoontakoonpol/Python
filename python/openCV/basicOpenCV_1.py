import cv2
print(cv2.__version__)

img = cv2.imread("/home/pitoon/snap/python/openCV/4.2.0/230501201_1.jpg", 0)
cv2.imshow('Show Image ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.jpg', img)