import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

board.analog[0].enable_reporting()
it = pyfirmata.util.Iterator(board)
it.start()

while True:
    photoresistor_value = board.analog[0].read()
    print(photoresistor_value)
    time.sleep(0.5)  # sleep for 0.5 seconds


#import logging
#logging.basicConfig(level=logging.DEBUG)

#print(board.sp.isOpen())

#logging.debug(f'Photoresistor value: {photoresistor_value}')

#led = board.get_pin('d:13:o')
#led.write(1)