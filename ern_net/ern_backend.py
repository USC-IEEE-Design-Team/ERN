from posixpath import split
import serial
import smbus
import time
from gpiozero import Buzzer, LED
from time import sleep

bus = smbus.SMBus(1)
address = 0x2a

location = [0, 0]

buzzer = Buzzer(17)
led = LED(27)

ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

while True:
    zone_data=ser.readline()
    decoded_zone_data = zone_data.decode('utf-8')
    zone_pairs = None
    zone_pairs_split = []
    lats = []
    lngs = []
    
    if zone_data:
        print(decoded_zone_data)

        zone_pairs = decoded_zone_data.split(";")

        print(zone_pairs)

        for pair in zone_pairs[:-1]:
            split_pair = pair.split(",")

            print(split_pair)

            zone_pairs_split.append([float(split_pair[0]), float(split_pair[1])])

        for item in zone_pairs_split:
            lats.append(item[1])
            lngs.append(item[0])

        print(lats)
        print(lngs)

        if location[0] > min(lats) and location[0] < max(lats) and location[1] > min(lngs) and location[1] < max(lngs):
            print("Node is in evacuation zone")

    data = ""
    last_char = ""
    while last_char != "\n":
        last_char = chr(bus.read_byte(address))
        data += last_char
    data = data[:-1]
    split_data = data.split(",")

    location[0] = float(split_data[0])
    location[1] = float(split_data[1])

    print(location)

# buzzer.on()

# while True:
#     led.on()
#     sleep(1)
#     led.off()
#     sleep(1)
