# Easy Comms

Easy Comms is a simple MicroPython library for easily sending messages over UART connections from one device to another

## Demo Apps

There are two demo applications:

* [`pico_comms_a.py`](pico_comms_a.py) - Listens for messages and prints them on the console
* [`pico_comms_b.py`](pico_comms_b.py) - Sends messages, also listens and prints to the console
* [`led_server.py`](led_server.py) - Tells the led_client to blink an led based on the contents of a json formatted message
* [`led_client.py`](led_client.py) - Listens for commands over UART for blink on and off commands

### How to use the Demo Apps
Load either of the demo code `pico_comms_a.py` and `pico_comms_b.py` or `led_client.py` and `led_server.py` onto a pair of Raspberry Pi Picos, and wire them us such that the GPIO Pin 0 (RX) goes to GPIO Pin 1 (TX) on the other Pico and vice versa. Also make sure both Picos have their grounds connected otherwise you'll get all kind of wierd messages and errors.

