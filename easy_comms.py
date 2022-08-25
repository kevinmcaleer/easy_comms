from machine import UART, Pin

class Easy_comms:
 
    uart_id = 0
    baud_rate = 9600
    
    def __init__(self, uart_id:int, baud_rate:int=None):
        self.uart_id = uart_id
        if baud_rate: self.baud_rate = baud_rate
        self.uart = UART(self.uart_id,self.baud_rate)
        self.uart.init()
        
    def send(self, message):
        print(f'sending message: {message}')
        self.uart.write(message)
        
    def start(self):
        message = "ahoy"
        print(message)
        self.send(message)

    def read(self)->str:
        if self.uart.any() > 0:
            return self.uart.read()
        else:
            return None
        