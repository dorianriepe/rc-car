from steering import Steering as Steering
from powertrain import Powertrain as Powertrain
from ultrasonic import Ultrasonic as Ultrasonic

import RPi.GPIO as IO


steering = Steering()
powertrain = Powertrain()
ultrasonic = Ultrasonic()

print("----------------------")
print("INSTRUCTIONS")
print("----------------------")
print("Forward:         'f'")
print("Backward:        'b'")
print("Stop:            's'")
print("----------------------")
print("Steering Left:   'l'")
print("Steering Middle: 'm'")
print("Steering Right:  'r'")
print("----------------------")



try:
    while True:
        value = input("Instruction: ")
        if value == "f":
            print("Forward")
            print()
            powertrain.forward(100)

        elif value == "b":
            print("Backward")
            print()
            powertrain.backwards(100)

        elif value == "s":
            print("Stop")
            print()
            powertrain.stop()

        elif value == "l":
            print("Steering Left")
            print()
            steering.left()

        elif value == "m":
            print("Steering Middle")
            print()
            steering.middle()

        elif value == "r":
            print("Steering Right")
            print()
            steering.right()
        else:
            print("Please choose one of the given commands.")
            print()
            powertrain.stop()
            steering.middle()


except KeyboardInterrupt:
    IO.cleanup()
    print("IO.cleanup")
