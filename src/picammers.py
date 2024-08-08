from picamera2 import Picamera2, Preview
import time
from PIL import Image
from pyzbar.pyzbar import decode
import os
import sys

def initialize_picam():
    time.sleep(1)
    ignore_stdout = sys.stdout
    sys.stdout = open('trash', 'w')
    picam2 = Picamera2()
    picam2.resolution = (1440, 1080)
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)},
    lores={"size": (640, 480)}, display="lores")
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    sys.stdout.close()
    sys.stdout = ignore_stdout
    return picam2


def capture_image(picam2):
    time.sleep(1)
    picam2.capture_file("barcode.jpg")
    return


def decode_barcode(file):
    image = Image.open(file)
    scanned_barcode = decode(image)
    barcode_data = 0 
    
    if (len(scanned_barcode) == 0):
        print ("no barcodes detected")
        scanned_barcode = 0
        return 0
        print(scanned_barcode)
    
    if (len(scanned_barcode) != 0):
        for barcode in scanned_barcode:
            barcode_data = barcode.data.decode()
            print("barcode information:", barcode_data)
            return barcode_data
    return

def close_picam():
    picam2 = Picamera2()
    picam2.close()

if __name__ == "_main_":
    fn = os.path.basename("barcode.jpg")
    initialize_picam()
    picam2 = initialize_picam()
    capture_image(picam2)
    decode_barcode(fn)