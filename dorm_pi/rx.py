
from serial import Serial as s

port=s(port="COM3",baudrate=57600)

while True:
    rb = port.read(25)
    print(rb)