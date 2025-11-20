#getting  sensor readings via usb

import serial 

ser = serial.Serial('/dev/ttyUSB0', 9600,  timeout=2)
def read_data():
    i = 0 
    while True:
        i+=1
        data = ser.readline().decode('utf').strip()
        values = [x.strip() for x in data.split(',')]
        
        try:
            if  i==10:          #taking the 10th reading to get a stable reading from sensor
                print(values)
                return values   # this also breaks the loop
        except Exception as e:
            print(e)

read_data()
