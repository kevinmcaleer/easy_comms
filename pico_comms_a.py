# Pico_comms_a
# Sends commands and listens to responses from pico_comms_b

from easy_comms import Easy_comms
from time import sleep
import json

com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

command = {'command':'glow', 'args': {'red':255, 'green':0, 'blue':0}}

com1.send(json.dumps(command))

while True:
    message = ""
    message = com1.read()
    
    if message is not None:
        print(f"message: {message.strip('\n')}")
    sleep(1)
