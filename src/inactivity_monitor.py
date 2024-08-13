import time
from threading import Event
from hal import hal_lcd as LCD

# Event to signal the inactivity timeout
inactivity_event = Event()
lcd = LCD.lcd()

def monitor_inactivity(last_activity_time, wakeup_event):
    """Thread function to monitor inactivity and stop the program after 60 seconds of inactivity."""
    while not inactivity_event.is_set():
        if time.time() - last_activity_time.value > 60:
            print("No activity for 60 seconds. Exiting...")
            lcd.lcd_clear()
            lcd.lcd_display_string("No activity",1)
            lcd.lcd_display_string("Shutting Down",2)
            time.sleep(3)
            lcd.backlight(0)
            wakeup_event.wait()
            wakeup_event.clear()
            last_activity_time.value = time.time() #reset timer on wake-up
        time.sleep(1)  # Check every second