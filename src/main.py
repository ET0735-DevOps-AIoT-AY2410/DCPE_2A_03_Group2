from hal import hal_lcd as LCD 
from hal import hal_keypad as keypad
from threading import Thread
import time
import queue
import readkey as key
import rfid as rfid

lcd = LCD.lcd()
shared_keypad_queue = queue.Queue()

def main():
    
    key.key_reader()

    while(True): 
        lcd.lcd_display_string("1. Scanner Start",1)
        lcd.lcd_display_string("2. Power Off",2)

        if key.ret_key() == 1:
            lcd.lcd_display_string("1. Scan ready",1)
            lcd.lcd_display_string("3 - pay",2)

            if key.ret_key() == 3: # to be replaced with PICAM
                lcd.clear()
                lcd.lcd_display_string("1 - PAYWAVE",1)
                lcd.lcd_display_string("2 - ATMPIN",2)

                if key.ret_key() == 2:
                    lcd.clear()
                    lcd.lcd_display_string("ATMPIN Selected",1)
                    #input rfid code
                    #input atm card code

                    
                    
        if keyvalue == 2:
            lcd.lcd_display_string("Powering Off",1)
            time.sleep(2)
            lcd.lcd_clear()
            lcd.backlight(0)




if __name__ == "__main__":
    main()