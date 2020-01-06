import RPi.GPIO as GPIO
import time

# PINS
PWM1 = 18
M1_A = 14
M1_B = 15

PWM2 = 25
M2_A = 8
M2_B = 7


# SETUP
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(M1_A, GPIO.OUT)
GPIO.setup(M1_B, GPIO.OUT)

GPIO.setup(PWM2, GPIO.OUT)
GPIO.setup(M2_A, GPIO.OUT)
GPIO.setup(M2_B, GPIO.OUT)




# OUTPUT

# forward
#GPIO.output(PWM2, GPIO.HIGH)
#GPIO.output(M2_A, GPIO.HIGH)
#GPIO.output(M2_B, GPIO.LOW)



# links
GPIO.output(PWM1, GPIO.HIGH)
GPIO.output(M1_A, GPIO.HIGH)
GPIO.output(M1_B, GPIO.LOW)

time.sleep(0.175)

GPIO.output(PWM1, GPIO.LOW)
GPIO.output(M1_A, GPIO.LOW)
GPIO.output(M1_B, GPIO.LOW)

time.sleep(3)


GPIO.output(PWM1, GPIO.HIGH)
GPIO.output(M1_A, GPIO.LOW)
GPIO.output(M1_B, GPIO.HIGH)

time.sleep(0.042)

GPIO.output(PWM1, GPIO.LOW)
GPIO.output(M1_A, GPIO.LOW)
GPIO.output(M1_B, GPIO.LOW)

time.sleep(3)

# backward
#GPIO.output(PWM2, GPIO.HIGH)
#GPIO.output(M2_A, GPIO.LOW)
#GPIO.output(M2_B, GPIO.HIGH)

# rechts
GPIO.output(PWM1, GPIO.HIGH)
GPIO.output(M1_A, GPIO.LOW)
GPIO.output(M1_B, GPIO.HIGH)

time.sleep(0.15)

GPIO.output(PWM1, GPIO.LOW)
GPIO.output(M1_A, GPIO.LOW)
GPIO.output(M1_B, GPIO.LOW)

time.sleep(3)


GPIO.output(PWM1, GPIO.HIGH)
GPIO.output(M1_A, GPIO.HIGH)
GPIO.output(M1_B, GPIO.LOW)

time.sleep(0.07)


GPIO.output(PWM1, GPIO.LOW)
GPIO.output(M1_A, GPIO.LOW)
GPIO.output(M1_B, GPIO.LOW)



# stop
#GPIO.output(PWM2, GPIO.LOW)
#GPIO.output(M2_A, GPIO.LOW)
#GPIO.output(M2_B, GPIO.LOW)



# CLEANUP
GPIO.cleanup()
