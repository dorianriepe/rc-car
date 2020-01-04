import keyboard  # using module keyboard
import time
import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

try:
    while True:  # making a loop

        sec = time.ctime()

        stdscr.clear()
        stdscr.refresh()
        print("Distance to Object: 73.2")
        print(sec)

        # Initial Position
        if not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Initial Position")
            time.sleep(1)


        # Forward
        elif keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Forward	Middle")
            time.sleep(1)

        elif keyboard.is_pressed('w') and keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Forward	Left")
            time.sleep(1)

        elif keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            print("Forward	Right")
            time.sleep(1)

        
        # Backward
        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Backward	Middle")
            time.sleep(1)

        elif not keyboard.is_pressed('w') and keyboard.is_pressed('a') and keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Backward	Left")
            time.sleep(1)

        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            print("Backward	Right")
            time.sleep(1)

        
        # Only Steering
        elif not keyboard.is_pressed('w') and keyboard.is_pressed('a') and not keyboard.is_pressed('s') and not keyboard.is_pressed('d'):
            print("Steering Left")
            time.sleep(1)

        elif not keyboard.is_pressed('w') and not keyboard.is_pressed('a') and not keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            print("Steering Right")
            time.sleep(1)

        
        # Exceptions

        else:
            print ("Do nothing")
            time.sleep(1)

        stdscr.refresh()


except KeyboardInterrupt:
        curses.endwin()