from picamera2 import Picamera2
import time
from model import model
def camera():

    cam = Picamera2()

    config = cam.create_still_configuration()
    cam.configure(config)

    cam.start()

    time.sleep(1)

    cam.capture_file("image.jpg")

    print("saved")
    model()

camera()# temporary to be removed
