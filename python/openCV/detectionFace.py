import cv2
print(cv2.__version__)

img = cv2.imread("/home/pitoon/snap/python/openCV/4.2.0/230501201_1.jpg", 1)
img = cv2.line(img,(0,0),(255,255),(255,0,),10) #(image, Start(x,y), End(x,y), (BGR), wieghtLine)
img = cv2.arrowedLine(img,(30,0),(455,455),(0,0,255),10) #(image, Start(x,y), End(x,y), (BGR), wieghtLine)
img = cv2.rectangle(img, (384,333),(510,128), (255,0,0),3)
img = cv2.circle(img,(447,63), 63, (0,255,0), 3) #(img, (center), radins, )
img = cv2.putText(img, "OpenCV", (10,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1) #(img, String, Font type, weight, color, bole)
cv2.imshow('Show Image ', img)

cv2.waitKey(0)
cv2.destroyAllWindows()