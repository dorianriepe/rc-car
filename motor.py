import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)
ENABLE = 18
INA = 14
INB = 15

print("Setup")
IO.setup(ENABLE, IO.OUT)
IO.setup(INA, IO.OUT)
IO.setup(INB, IO.OUT)

print("Output")
IO.output(ENABLE, IO.HIGH)
IO.output(INA, IO.LOW)
IO.output(INB, IO.HIGH)

print("Sleep")
time.sleep(2)

print("Clean up")
IO.cleanup()
