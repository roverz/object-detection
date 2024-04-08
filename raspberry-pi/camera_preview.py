import cv2
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (2592,1944)}))
picam2.start()
while True :
    im = picam2.capture_array()
    cv2.imshow("camera", im)
    cv2.waitKey(1)
