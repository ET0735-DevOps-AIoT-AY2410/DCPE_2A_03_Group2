from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread
import time
import queue

lcd = LCD.lcd()

shared_keypad_queue = queue.Queue()

def key_pressed(key):
    shared_keypad_queue.put(key)

def key_reader():
    keypad.init(key_pressed)
    keypad_thread = Thread.Thread(target = keypad.get_key)
    keypad_thread.start()


def ret_key():
    keyvalue = shared_keypad_queue.get()
    return keyvalue


def clear_queue():
    while not shared_keypad_queue.empty():
        shared_keypad_queue.get()

def get_item_by_position(position):
    items = []
    item = None

    for _ in range(position + 1):
        item = shared_keypad_queue.get()
        items.append(item)
    for item in items:
        shared_keypad_queue.put(item)
    return items[position]
