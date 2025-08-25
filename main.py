# Basic experimentation with OpenCV
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('Test',frame)
    if cv2.waitKey(1) & 0xFF == 27: # Press 'ESC' to exit
        break
cap.release()
cv2.destroyAllWindows()

## Checkking for Webcam Access
