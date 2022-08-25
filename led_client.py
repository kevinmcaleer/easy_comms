# led_client

from easy_comms import Easy_comms
from time import sleep
from machine import Pin

com1 = Easy_comms(0,9600)
led = Pin("LED", Pin.OUT, value=0)

while true:
    if message is not None:
        if message['command'] == 'blink':
            if message['args'] == 'on':
                led.on()
            if message['args'] == 'off':
                led.off()
    sleep(1)
        

