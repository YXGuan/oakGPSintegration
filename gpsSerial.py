# you need to connect GPS receiver to USB to run following code

import serial
import datetime

ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
ser.flushInput()
ser.flushOutput()
idx = 0

nmea_data = b""

# skip first line, since it could be incomplete
ser.readline()

while True:
    idx += 1
    nmea_sentence = ser.readline()
    nmea_data += nmea_sentence
    print(nmea_data)
    if idx % 100 == 0:
        print(f"idx: {idx}")
        
    if idx % 2000 == 0:

        # save to file after 2000 sentences added
        filename = datetime.datetime.utcnow().strftime("data/gps_data_%Y%m%d-%H%M%S.nmea")
        f = open(filename, "ab")
        f.write(nmea_data)
        f.close()
        
        nmea_data = b""