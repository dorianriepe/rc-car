import time
import RPi.GPIO as GPIO
from steering import Steering as Steering
from powertrain import Powertrain as Powertrain
from ultrasonic import Ultrasonic as Ultrasonic

# init
steering = Steering()
powertrain = Powertrain()
ultrasonic = Ultrasonic()


while True:
    dist = ultrasonic.distance()
    print(dist)
    if dist > 40:
        powertrain.forward(100)
        time.sleep(0.5)
    else:
        powertrain.stop()
        GPIO.cleanup
        break
