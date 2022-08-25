# Pico_comms_b
# Sends commands and listens to responses from pico_comms_a

from easy_comms import Easy_comms
from time import sleep

com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

count = 0
while True:
    # send a message
    com1.send(f'hello, {count}')
    
    #check for messages
    message = com1.read()
    
    if message is not None:
        print(f"message received: {message.strip('\n')}")
    sleep(1)
    count +=1
