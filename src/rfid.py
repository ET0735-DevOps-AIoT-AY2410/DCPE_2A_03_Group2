import RPI.GPIO as GPIO
import signal
import time
import sys
from hal import hal_rfid_reader as rfid_reader

def read_rfid(reader):
    ignore_stdout = sys.stdout
    sys.stdout = open('trash', 'w')
    var1 = reader.read()
    sys.stdout.close()
    sys.stdout = ignore_stdout
    #rfid output [uid, card info, Pin]
    print(var1)
    #clean list
    var1 = [str(item) for item in var1  ] #convert item to string
    cleaned_var1 = [item.strip(' ') for item in var1]
    var2 = cleaned_var1[1]
    split_var2 = var2.split(',')
    uid = cleaned_var1[0]

    try:
        card_info = [int(item) for item in split_var2[:-1]]
    except ValueError:
        card_info = [float(item) for item in split_var2[:-1]]
    pin = split_var2[-1]

    return uid

if __name__ == "__main__":
    reader = rfid_reader.init()
    read_rfid(reader)




