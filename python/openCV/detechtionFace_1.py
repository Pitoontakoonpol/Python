import cv2

faceCascade = cv2.CascadeClassifier("/home/pitoon/snap/python/openCV/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")

def drawBoundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gary, scaleFactor, minNeighbors)
    coords = []
    for (x, y, weight, hight) in features:
        cv2.rectangle(img, (x,y), (x + weight, y + hight), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
    return img

def detect(img, faceCascade):
    img = drawBoundary(img, faceCascade, 1.1, 10, (255,0,0), "Face")
    return img

cap = cv2.VideoCapture('Accenture-Human-Machine-AI-James.png')
while (True):
    ret,frame = cap.read()
    frame = detect(frame, faceCascade)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame: ',gray)
    if(cv2.waitKey(0) & 0xFF == ord('q')):
        break
    # if(cv2.waitKey(0)):
    #     break

#https://github.com/kongruksiamza/Open...
#Object Detection Blog : https://www.bogotobogo.com/python/Ope...
#OpenCV Haarcascades : https://github.com/opencv/opencv/tree...
    
cap.release()
cv2.destroyAllWindows()