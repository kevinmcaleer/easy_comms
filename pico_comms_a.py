# Pico_comms_a
# Sends commands and listens to responses from pico_comms_b

# from machine import UART, Pin
from easy_comms import Easy_comms
from time import sleep

com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

while True:
    message = ""
    message = com1.read()
    
    if message is not None:
        new_message = str(message)
        print(new_message)
    sleep(1)

# RX = Pin(0)
# TX = Pin(1)
# ID = 0
# uart = UART(id=ID,rx=RX, tx=TX)

# command = [['command':'change colour'],['args':{'red':255, 'green':255, 'blue':0}]]

# print(f"command: {command['command']}")

# def send_command(cmd):
#     uart.send(cmd)    
# 
# while True or KeyboardInterupt:
#     send_command(command)
#     if uart.any():
#         print(uart.read())