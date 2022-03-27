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
    x=ser.readline()
    print(x)

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