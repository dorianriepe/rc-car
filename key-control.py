import keyboard  # using module keyboard
import time
import curses
import RPi.GPIO as IO

from steering import Steering as Steering
from powertrain import Powertrain as Powertrain 
from ultrasonic import Ultrasonic as Ultrasonic

steering = Steering()
powertrain = Powertrain()
ultrasonic = Ultrasonic()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

try:
    while True:  # making a loop

        sec = time.ctime()

        stdscr.clear()
        stdscr.refresh()
        
        dist = ultrasonic.distance()

        # Initial Position
        if not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Initial Position")
            print(dist)
            powertrain.stop()
            steering.middle()
            time.sleep(1)


        # Forward
        elif keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d') and dist > 40:
            print("Forward	Middle")
            print(dist)
            powertrain.forward(100)
            steering.middle()
            time.sleep(1)

        elif keyboard.is_pressed('w') and keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d') and dist > 40:
            print("Forward	Left")
            print(dist)
            powertrain.forward(100)
            steering.left()
            time.sleep(1)

        elif keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and keyboard.is_pressed('d') and dist > 40:
            print("Forward	Right")
            print(dist)
            powertrain.forward(100)
            steering.right()
            time.sleep(1)

        
        # Backward
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Backward	Middle")
            powertrain.backwards(100)
            steering.middle()
            time.sleep(1)

        elif not keyboard.is_pressed('w') and keyboard.is_pressed('a') and keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Backward	Left")
            powertrain.backwards(100)
            steering.left()
            time.sleep(1)

        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            print("Backward	Right")
            powertrain.backwards(100)
            steering.right()
            time.sleep(1)

        
        # Only Steering
        elif not keyboard.is_pressed('w') and keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Steering Left")
            powertrain.stop()
            steering.left()
            time.sleep(1)

        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            print("Steering Right")
            powertrain.stop()
            steering.right()
            time.sleep(1)

        
        # Exceptions

        else:
            print ("Initial Position")
            print(dist)
            powertrain.stop()
            steering.middle()
            time.sleep(1)

        stdscr.refresh()


except KeyboardInterrupt:
        IO.cleanup()
        curses.endwin()
