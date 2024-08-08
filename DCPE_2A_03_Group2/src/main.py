from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread
import time
import queue
import readkey as key
import rfid as rfid
from hal import hal_rfid_reader as rfid_reader
import csv
import time
import zbarlight
from picamera import PiCamera
from PIL import Image
import RPi as GPIO

# Setup
camera = PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Assuming button is connected to GPIO pin 3
database = {}

card_pin = 1234

lcd = LCD.lcd()
shared_keypad_queue = queue.Queue()

# Load the database
with open('gr_database.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row
    for rows in reader:
        name, price = rows
        database[name] = float(price)

total_price = 0

def picam():
    global total_price
    while True:
        camera.capture('barcode.jpg')
        with open('barcode.jpg', 'rb') as image_file:
            image = Image.open(image_file)
            image.load()
        codes = zbarlight.scan_codes('ean13', image)
        if codes:
            code = codes[0].decode('utf-8')  # Assuming the barcode text is utf-8 encoded
            name, quantity = code.split(',')
            if name in database:
                item_price = database[name] * int(quantity)
                total_price += item_price
                lcd.lcd_display_string(f"{name.upper()} ${item_price}", 1)
                time.sleep(1)
                lcd.lcd_display_string(f"TOTAL PRICE ${total_price}", 1)
                lcd.lcd_display_string("3. PAY", 2)
                if GPIO.input(3) == GPIO.LOW:
                    break
            else:
                lcd.lcd_display_string("ITEM NOT FOUND", 1)
                time.sleep(1)
        else:
            lcd.lcd_display_string("NO BARCODE FOUND", 1)
            time.sleep(1)
    lcd.lcd_clear()

def main():
    
    key.key_reader()
    reader = rfid_reader.init()

    while(True): 
        lcd.lcd_display_string("1. Scanner Start",1)
        lcd.lcd_display_string("2. Power Off",2)

        if key.ret_key() == 1:
            lcd.lcd_display_string("                    ",1)
            lcd.lcd_display_string("                    ",2)
            lcd.lcd_display_string("Scan Ready",1)
            lcd.lcd_display_string("3. Pay",2)
            try:
                picam()
            except KeyboardInterrupt:
                pass
            finally:
                GPIO.cleanup()
                lcd.lcd_display_string("                    ",1)
                lcd.lcd_display_string("                    ",2)
                camera.close()

            if key.ret_key() == 3: # to be replaced with PICAM
                lcd.lcd_display_string("                    ",1)
                lcd.lcd_display_string("                    ",2)
                lcd.lcd_display_string("1 - PAYWAVE",1)
                lcd.lcd_display_string("2 - ATMPIN",2)

                if key.ret_key() == 1:
                    lcd.lcd_display_string("                    ",1)
                    lcd.lcd_display_string("                    ",2)
                    lcd.lcd_display_string("Scan your card",1)
                    uid = rfid.rfid_reader(reader)
                    
                #input atm card code
                if key.ret_key() == 2:
                    lcd.lcd_display_string("                    ",1)
                    lcd.lcd_display_string("                    ",2)
                    lcd.lcd_display_string("Please Key in",1)
                    lcd.lcd_display_string("Your PIN",2)
                    if key.ATMPIN(card_pin) == True:
                        print("Success")
                        break
                        
        if key.ret_key() == 2:
            lcd.lcd_display_string("Powering Off",1)
            time.sleep(2)
            lcd.lcd_clear()
            lcd.backlight(0)

if __name__ == "__main__":
    main()