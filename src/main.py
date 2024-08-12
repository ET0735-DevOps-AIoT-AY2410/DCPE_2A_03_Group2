from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread, Event
import time
import queue
import readkey as key
from hal import hal_rfid_reader as rfid_reader
from hal import hal_buzzer as buzz
import csv
import time
import zbarlight
from picamera import PiCamera
from PIL import Image
import RPi as GPIO
import os
import picammers as pick
import glob
from inactivity_monitor import monitor_inactivity, inactivity_event
from multiprocessing import Value
picam2 = pick.initialize_picam()


database = {}
with open('gr_database.csv',mode ='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        database[row['product_ID']] = {'name': row['name'],'price': row['price']}


card_pin = 1234
total_price = 0.0


lcd = LCD.lcd()
shared_keypad_queue = queue.Queue()

last_activity_time = Value('d',time.time())
wakeup_event = Event()


def payment():
    lcd.lcd_clear()
    lcd.lcd_display_string("1. Scan Ready",1)
    lcd.lcd_display_string("3. Pay",2)
    if key.ret_key() == 1:
        wakeup_event.set() #wake system up if sleeping
        scan()
def home():
    lcd.lcd_clear()
    lcd.lcd_display_string("1. Scanner Start",1)
    lcd.lcd_display_string("2. Power off",2)
    if key.ret_key() == 1:
        wakeup_event.set()
        main()

def scan():
    global total_price
    print("Database contents: ")
    for product_id, value in database.items():
        print(f"Product ID: {product_id}, Item: {value}")

    lcd.lcd_clear()
    lcd.lcd_display_string("Please Wait...",1)
    barcode_data = 0
    fn = os.path.basename("barcode.jpg")
    condition_met = False
    while not condition_met:
        lcd.lcd_clear()
        lcd.lcd_display_string("Please Scan...",1)
        pick.capture_image(picam2)
        barcode_data = pick.decode_barcode(fn)
        print("scan in progress...")
        if barcode_data != 0:
            last_activity_time.value = time.time() #reset inactivity timer
            wakeup_event.set() #wake up system if sleeping
            print("success")
            files = glob.glob(os.path.join(fn, '*'))
            for file in files: #deletes barcode picture automatically
                try:
                    os.remove(file)
                    print(f"Deleted {file}")
                except Exception as e:
                    print(f"Error deleting file {file}: {e}")
             # Lookup item in the database
            if barcode_data in database:
                try:
                    item_info = database[barcode_data]
                    item_price = 0.0
                    item_name = item_info['name']
                    item_price = float(item_info['price'])
                    print(f"item price is {item_price}")
                    print(type(item_price))
                    
                    total_price = total_price + float(item_price)
                    print(f"total price is {total_price}")
                    print(type(total_price))
                    print(f"Item: {item_name}, Price: {item_price}")
                    
                    lcd.lcd_display_string(f"{item_name}: ${item_price}", 1)
                    lcd.lcd_display_string(f"Total: ${total_price}",2)
                    
                    buzz.turn_on_with_timer(2)
                    condition_met = True
                    
                except ValueError as e:
                    print(f"Error converting price to float: {e}")
            else:
                print(f"{barcode_data} not found.")
                lcd.lcd_display_string("Item not found", 1)
                time.sleep(2)
    time.sleep(5)
    payment()
        

def main():
    global total_price
    key.key_reader()
    reader = rfid_reader.init()
    buzz.init()
    
    inactivity_thread = Thread(target=monitor_inactivity, args=(last_activity_time, wakeup_event))
    inactivity_thread.start()

    while(True): 
        lcd.lcd_display_string("1. Scanner Start",1)
        lcd.lcd_display_string("2. Power Off",2)

        if key.ret_key() == 1:
            total_price = 0.0 #reset for new customer
            last_activity_time.value = time.time()
            lcd.lcd_clear()
            lcd.lcd_display_string("1, Scan Ready",1)
            lcd.lcd_display_string("3. Pay",2)
            
            if key.ret_key() == 1:
                scan()
            
            if key.ret_key() == 3: # to be replaced with PICAM
                lcd.lcd_clear()
                lcd.lcd_display_string("1 - PAYWAVE",1)
                lcd.lcd_display_string("2 - ATMPIN",2)
               
                if key.ret_key() == 1:
                    last_activity_time.value = time.time()
                    wakeup_event.set() #wake system up if sleeping
                    lcd.lcd_clear()
                    lcd.lcd_display_string("Scan your card",1)
                    uid = reader.read_id_no_block()
                    buzz.turn_on_with_timer(2)
                    uid = str(uid)
                    if uid != "None":
                        print("RFID card ID = " + uid)
                        # Display RFID card ID on LCD line 2
                        lcd.lcd_clear()
                        lcd.lcd_display_string(uid, 1)
                        lcd.lcd_display_string("Payment Success",2)
                        time.sleep(2)
                        lcd.lcd_clear()
                        home()
                #input atm card code
                if key.ret_key() == 2:
                    last_activity_time.value = time.time()
                    wakeup_event.set()
                    lcd.lcd_clear()
                    isvalid = True
                    while(isvalid == True):
                        lcd.lcd_display_string("Please Key in PIN",1)
                        lcd.lcd_display_string("press # when done",2)
                        time.sleep(2)
                        lcd.lcd_clear()
                        
                        if key.ATMPIN(card_pin):
                            print("Success")
                            lcd.lcd_clear()
                            buzz.turn_on_with_timer(2)
                            lcd.lcd_display_string("Payment Success",1)
                            time.sleep(2)
                            lcd.lcd_clear()
                            isvalid = False
                            home()
                        else:
                            print("Incorrect PIN")
                            lcd.lcd_display_string("Incorrect.",1)
                            lcd.lcd_display_string("Try again.",2)
                            isvalid = True
                        
                    
        if key.ret_key() == 2:
            lcd.lcd_clear()
            lcd.lcd_display_string("Powering Off",1)
            time.sleep(1)
            lcd.lcd_clear()
            lcd.backlight(0)
        
            if key.ret_key() == 1:
                lcd.lcd_clear()
                lcd.lcd_display_string("Starting...",1)
                time.sleep(1)
                lcd.lcd_clear()
                lcd.backlight(1)
                main()

if __name__ == "__main__":
    main()