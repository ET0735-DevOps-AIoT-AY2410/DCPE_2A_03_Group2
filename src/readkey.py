from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread
from hal import hal_buzzer as buzz
import time
import queue

lcd = LCD.lcd()

shared_keypad_queue = queue.Queue()

def key_pressed(key):
    shared_keypad_queue.put(key)

def key_reader(): #scans the keypad
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

def ret_key(): #returns value
    keyvalue = shared_keypad_queue.get()
    return keyvalue

def ATMPIN(card_no): #to allow key input for card payment
    clear_queue()
    
    expected_length = len(str(card_no))
    PIN =[]
    
    while len(PIN) < expected_length+1:
        key = shared_keypad_queue.get()
        
        key_str = str(key)
        
        if  (key_str.isdigit() or key_str=="#"):
            PIN.append(key_str)
            lcd.lcd_display_string("".join(PIN),1)
        
        #Display the entered key (optional, for debugging)
            print(f"Key entered: {''.join(PIN)}")
    entered_pin = "".join(PIN)
    print(f"Entered PIN: {entered_pin}")
        
        
    if entered_pin[:-1] ==str(card_no) and entered_pin[-1] == "#":
        print("correct pin entered")
        return True
    else:
        return False

def clear_queue(): #clears the items in the queue
    while not shared_keypad_queue.empty():
        shared_keypad_queue.get()

def get_item_by_position(position): #find the position of a item in the queue
    items = []
    item = None

    for _ in range(position + 1):
        item = shared_keypad_queue.get()
        items.append(item)
    for item in items:
        shared_keypad_queue.put(item)
    return items[position]

if __name__ == "__main__":
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    buzz.init()








    














