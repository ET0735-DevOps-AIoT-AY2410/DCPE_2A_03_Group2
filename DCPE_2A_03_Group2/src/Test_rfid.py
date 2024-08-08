import rfid
from hal import hal_rfid_reader as rfid_reader
import sys
from io import StringIO



def test_rfid_reader():
    reader = rfid_reader.init()
   
    
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out

        uid = rfid.read_rfid(reader)

        assert(isinstance(uid,str) and len(uid)>0)

    finally:
        sys.stdout = saved_stdout

    
    