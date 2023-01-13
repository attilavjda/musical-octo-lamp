import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
it = pyfirmata.util.Iterator(board)
it.start()

prev_time = time.time()
print("prev time = time.time(): ", prev_time)

while True:
    
    time.sleep(0.5)  # sleep for 0.5 seconds, photoresistors have a chance to provide reading
    
    # create two values for the averages of every 10 photoresistor readings
    values1 = []
    values2 = []
    for i in range(10):
        values1.append(board.analog[0].read())
        values2.append(board.analog[1].read())
        time.sleep(0.1)
    photoresistor1_value = sum(values1)/10
    photoresistor2_value = sum(values2)/10
    print("photoresistor1_value:", photoresistor1_value,"photoresistor2_value:", photoresistor2_value)

    if photoresistor1_value is not None and photoresistor1_value is not None:
       
        delta_s = photoresistor2_value - photoresistor1_value  # calculate difference of photoresistor readings
        print("delta s: ", delta_s)
        
        current_time = time.time() # increment current_time with the change since last reading of time
        print("current_time = time.time(): ", current_time)

        delta_t = current_time - prev_time # change of time
        print("delta_t = current_time - prev_time: ", delta_t)

        prev_time = current_time
        velocity = delta_s/delta_t # velocity is the change of position divided by change in time
        print("prev_time = current_time: ", prev_time)
        print("velocity = delta_s/delta_t:", velocity)