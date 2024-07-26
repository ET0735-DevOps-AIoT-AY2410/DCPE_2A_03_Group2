from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread
import time
import queue
import readkey as key

lcd = LCD.lcd()

shared_keypad_queue = queue.Queue()



def main():
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    keyvalue = shared_keypad_queue.get()

    while(True): 
        lcd.lcd_display_string("1. Scanner Start",1)
        lcd.lcd_display_string("2. Power Off",2)

        if keyvalue == 1:
            lcd.lcd_display_string("1. Scan ready",1)
            lcd.lcd_display_string("3 - pay",2)

            if keyvalue == 3:
                lcd.clear()
                lcd.lcd_display_string("1 - PAYWAVE",1)
                lcd.lcd_display_string("2 - ATMPIN",2)

                if keyvalue == 2:
                    lcd.clear()
                    lcd.lcd_display_string("ATMPIN Selected",1)
                    key.clear_queue()
                    print(shared_keypad_queue.empty())
                    queue_length = shared_keypad_queue.qsize()
                    if queue_length != 6 and key.get_item_by_position(6)!="#":
                        shared_keypad_queue.put(keyvalue)
                    else:

                    
                    
        if keyvalue == 2:
            lcd.lcd_display_string("Powering Off",1)
            time.sleep(2)
            lcd.lcd_clear()
            lcd.backlight(0)




if __name__ == "__main__":
    main()