## REQUIREM ##
#pip install pyzbar
#pip install opencv-python
#pip install picamera[array]

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

def main():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    raw_capture = PiRGBArray(camera, size=(640, 480))
    
    time.sleep(0.1)  # Allow camera to warm up

    print("Press 'Ctrl+C' to quit.")
    try:
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
            img = frame.array
            
            for code in decode(img):
                print(code.data.decode("utf-8"))
            
            cv2.imshow("image", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            raw_capture.truncate(0)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        camera.close()

if __name__ == "__main__":
    main()