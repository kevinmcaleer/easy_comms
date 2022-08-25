# led_server

from easy_comms import Easy_comms
from time import sleep
from machine import Pin
import json

command = {'command':'blink', 'args': 'on'}

com1 = Easy_comms(0,9600)
led = Pin(25, Pin.OUT)

while True:
    com1.send(str(json.dumps(command)))
    if command['args'] == 'on':
       command = {'command':'blink', 'args': 'off'}
    else:
       command = {'command':'blink', 'args': 'on'}
    led.toggle()
    sleep(1)
