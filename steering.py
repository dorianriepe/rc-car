import RPi.GPIO as GPIO
import time

# PINS
ENABLE_1 = 18
OUTPUT_1 = 15
OUTPUT_2 = 14


# SETUP
GPIO.setmode(GPIO.BCM)

GPIO.setup(ENABLE_1, GPIO.OUT)
GPIO.setup(OUTPUT_1, GPIO.OUT)
GPIO.setup(OUTPUT_2, GPIO.OUT)


# VARIABLES
position = ""


# MAIN
class Steering:
    def __init__(self):
        print("Setup steering")
        self.position = "middle"


    def left(self):
        if self.position == "middle":
            
            print("Middle -> Left")
            # -> left
            GPIO.output(ENABLE_1, GPIO.HIGH)
            GPIO.output(OUTPUT_1, GPIO.HIGH)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            
            time.sleep(0.175)
            
            GPIO.output(ENABLE_1, GPIO.LOW)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            self.position = "left"
            

        elif self.position == "left":
            print("Left -> Left")
            self.position = "left"


        elif self.position == "right":
            
            print("Right -> Left")
            # -
            GPIO.output(ENABLE_1, GPIO.HIGH)
            GPIO.output(OUTPUT_1, GPIO.HIGH)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            
            time.sleep(0.245) # 175+70
            
            GPIO.output(ENABLE_1, GPIO.LOW)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            self.position = "left"


    def middle(self):
        if self.position == "middle":
            print("Middle -> Middle")
            self.position = "middle"
            
        elif self.position == "left":
            print ("Left -> Middle")
            self.position = "middle"
            
            GPIO.output(ENABLE_1, GPIO.HIGH)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.HIGH)
            
            time.sleep(0.042)
            
            GPIO.output(ENABLE_1, GPIO.LOW)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.LOW)

        elif self.position == "right":
            print("Right -> Middle")
            GPIO.output(ENABLE_1, GPIO.HIGH)
            GPIO.output(OUTPUT_1, GPIO.HIGH)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            
            time.sleep(0.070)
            
            GPIO.output(ENABLE_1, GPIO.LOW)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            self.position = "middle"


    def right(self):
        if self.position == "middle":
            print("Middle -> Right")
            GPIO.output(ENABLE_1, GPIO.HIGH)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.HIGH)
            
            time.sleep(0.150)
            
            GPIO.output(ENABLE_1, GPIO.LOW)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            self.position = "right"

        elif self.position == "left":
            print ("Left -> Right")
            GPIO.output(ENABLE_1, GPIO.HIGH)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.HIGH)
            
            time.sleep(0.192)
            
            GPIO.output(ENABLE_1, GPIO.LOW)
            GPIO.output(OUTPUT_1, GPIO.LOW)
            GPIO.output(OUTPUT_2, GPIO.LOW)
            self.position = "right"
            

        elif self.position == "right":
            print("Right -> Right")
            self.position = "right"
