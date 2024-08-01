from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread
import time
import queue

lcd = LCD.lcd()

shared_keypad_queue = queue.Queue()

def key_pressed(key):
    shared_keypad_queue.put(key)

def key_reader(): #scans the keypad
    keypad.init(key_pressed)
    keypad_thread = Thread.Thread(target = keypad.get_key)
    keypad_thread.start()


def ret_key(): #returns value
    keyvalue = shared_keypad_queue.get()
    return keyvalue

def ATMPIN(card_no): #to allow key input for card payment
    PIN = []
    while (len(PIN)< len(int(i) for i in str(card_no))):
        key = shared_keypad_queue.get() 
        PIN.append(key)

    if (len(PIN) == len(int(i) for i in str(card_no))):
        if PIN.index("#")!=6 :
            return False
        if len(PIN)>7 :
            return False
        else:
            return True
 def ret_key_no_wait():
    try:
        keyvalue = share_keypad_queue.get_nowait()
        
    except queue.Empty:
        return None
    return keyvalue


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
    keypad_thread = Thread( target=keypad.get_key )
    keypad_thread.start()








    














