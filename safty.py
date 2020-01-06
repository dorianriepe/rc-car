import time
import RPi.GPIO as IO
from ultrasonic import Ultrasonic as Ultrasonic
from powertrain import Powertrain as Powertrain
ultrasonic = Ultrasonic()
powertrain = Powertrain()

try:
    while True:
        dist = ultrasonic.distance()
        print(dist)
        if dist < 40:
            powertrain.stop()
        time.sleep(0.2)
except KeyboardInterrupt:
    IO.cleanup()
