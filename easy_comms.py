#Easy comms is a simple class that allows you to send and receive messages over a serial port.

from machine import UART, Pin
from time import time_ns

class Easy_comms:
 
    uart_id = 0
    baud_rate = 9600
    timeout = 1000 # milliseconds
    
    def __init__(self, uart_id:int, baud_rate:int=None):
        self.uart_id = uart_id
        if baud_rate: self.baud_rate = baud_rate

        # set the baud rate
        self.uart = UART(self.uart_id,self.baud_rate)

        # Initialise the UART serial port
        self.uart.init()
            
    def send(self, message:str):
        print(f'sending message: {message}')
        message = message + '\n'
        self.uart.write(bytes(message,'utf-8'))
        
    def start(self):
        message = "ahoy\n"
        print(message)
        self.send(message)

    def read(self)->str:
        start_time = time_ns()
        current_time = start_time
        new_line = False
        message = ""
        while (not new_line) or (current_time <= (start_time + self.timeout)):
            if (self.uart.any() > 0):
                message = message + self.uart.read().decode('utf-8')
                if '\n' in message:
                    new_line = True
                    message = message.strip('\n')
                    # print(f'received message: {message}')
                    return message
        else:
            return None
        