import csv
from picamera2 import PiCamera2
from PIL import Image
from pyzbar.pyzbar import decode
import os
import sys

# Setup
def init_picam():
    time.sleep(5)
    ignore_stdout = sys.stdout
    sys.stdout = open('trash','w')
    picam1 = Picamera2()
    picam2.resolution = (1440, 1080)
    camera_config = picam2.create_still_configuration(main={"size": (640,480)},display="lores")
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    sys.stdout = ignore_stdout
    return picam2

def cap_img(picam2):
    time.sleep(3)
    picam2.capturefile("barcode.jpg")
    
def dec_bar(file):
    image = Image.open(file)
    scanned_barcode = deconde(image)
    barcode_data = 0
    
    if (len(scanned_barcode) == 0):
        print ("None detected.")
        return "no barcodes detected"
    
    for barcode in scanned_barcode:
        barcode_data = barcode.data.decode()
        print(barcode_data)
        return barcode_data

#if_name_=="_main_":
    #fn = os.path.basename("barcode.jpg")