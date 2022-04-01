#!/usr/bin/python

import smbus
import time
bus = smbus.SMBus(1)
address = 0x2a

while True:
    data = ""
    last_char = ""
    while last_char != "\n":
        last_char = chr(bus.read_byte(address))
        data += last_char
    print(data)
    time.sleep(1)