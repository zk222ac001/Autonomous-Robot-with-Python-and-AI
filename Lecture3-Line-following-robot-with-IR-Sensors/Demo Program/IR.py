'''
Physical Pin 1 --> 5V
Physical Pin 6 --> Ground
Physical Pin 11 ---> 1 ohm + 2 ohm 

'''

# RPi.GPIO allows Python to control and read the Raspberry
# Pi’s GPIO pins , as GPIO gives the library a shorter name.
# For example, you write GPIO.input().
import RPi.GPIO as GPIO
# time provides the sleep() function, which pauses the program.
import time
# IR_PIN stores the GPIO number connected to the sensor’s OUT pin.
IR_PIN = 17  # BCM GPIO17 = physical pin 11
# register BCM mode
GPIO.setmode(GPIO.BCM)

'''
This configures GPIO17 to receive a signal from the sensor.
The sensor produces an electrical signal at its OUT pin.
The Raspberry Pi reads that signal through its GPIO input.
'''

GPIO.setup(IR_PIN, GPIO.IN)  # Read the sensor's output

try:
    while True:
        '''
           GPIO.input(IR_PIN) reads the digital logic level on GPIO17 and
           stores the result in sensor_value.
           Reading	 GPIO constant	Meaning as an electrical signal
           0	     GPIO.LOW	    Low logic level
           1	     GPIO.HIGH	    High logic level
        '''
        # This reads a digital state, not a distance or an exact voltage.
        sensor_value = GPIO.input(IR_PIN)
        # Many IR obstacle modules are active LOW:
        # LOW (0) = object detected
        # HIGH (1) = no object detected
        if sensor_value == GPIO.LOW:
            print("Object detected!")
        else:
            print("No object detected.")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    GPIO.cleanup()