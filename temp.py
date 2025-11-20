from picamera2 import Picamera2
import cv2

picam = Picamera2()

picam.configure(picam.preview_configuration)
picam.start()

while "a":
    frame = picam.capture_array()
    cv2.imshow("Live Camera Feed" , frame)


