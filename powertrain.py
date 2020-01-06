import RPi.GPIO as GPIO

# PINS
ENABLE_2 = 25
OUTPUT_3 = 7
OUTPUT_4 = 8

# SETUP
GPIO.setmode(GPIO.BCM)

GPIO.setup(ENABLE_2, GPIO.OUT)
GPIO.setup(OUTPUT_3, GPIO.OUT)
GPIO.setup(OUTPUT_4, GPIO.OUT)

pwm = GPIO.PWM(ENABLE_2, 50)  # frequency=50Hz


# MAIN
class Powertrain:
    def __init__(self):
        print("Setup powertrain")

    def forward(self, speed):
        #speed = speed/100
        print(speed)
        pwm.start(0)
        
        GPIO.output(ENABLE_2, GPIO.HIGH)
        GPIO.output(OUTPUT_3, GPIO.HIGH)
        GPIO.output(OUTPUT_4, GPIO.LOW)
        pwm.ChangeDutyCycle(speed)

    def backwards(self, speed):
        print(speed)
        pwm.start(0)
        
        GPIO.output(ENABLE_2, GPIO.HIGH)
        GPIO.output(OUTPUT_3, GPIO.LOW)
        GPIO.output(OUTPUT_4, GPIO.HIGH)
        pwm.ChangeDutyCycle(speed)

    def changeFrequency(self, freq):
        pwm.ChangeFrequency(freq)

    def stop(self):
        GPIO.output(ENABLE_2, GPIO.LOW)
        GPIO.output(OUTPUT_3, GPIO.LOW)
        GPIO.output(OUTPUT_4, GPIO.LOW)
        pwm.stop()
