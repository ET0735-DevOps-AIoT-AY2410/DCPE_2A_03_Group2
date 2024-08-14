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


def capture_image(picam2, file_path="barcode.jpg"):
    time.sleep(1)
    picam2.capture_file(file_path)
    return file_path


def decode_barcode(file_path):
    try:
        image = Image.open(file_path)
        scanned_barcode = decode(image)
        
        if not scanned_barcode:
            print("No barcodes detected")
            return None
        
        for barcode in scanned_barcode:
            barcode_data = barcode.data.decode()
            print("Barcode information:", barcode_data)
            return barcode_data

    except Exception as e:
        print(f"Error decoding barcode: {e}")
        return None

def close_picam():
    picam2 = Picamera2()
    picam2.close()

if __name__ == "_main_":
    picam2 = initialize_picam()
    file_path = capture_image(picam2)
    barcode_data = decode_barcode(file_path)
    close_picam(picam2)
    if barcode_data:
        print(f"Decoded barcode: {barcode_data}")
    else:
        print("No barcode data found.")
