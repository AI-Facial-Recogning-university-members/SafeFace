import face_recognition
import cv2

camera = cv2.VideoCapture(0)

while True:
    verifcacao, frame = camera.read()
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(5)
    
    if key == 27:
        break