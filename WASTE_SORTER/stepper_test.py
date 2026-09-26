import RPi.GPIO as GPIO
import time

step_pin = 2
dir_pin = 3
steps_per_revolution = 200

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

GPIO.output(dir_pin, GPIO.HIGH)

try:
    while True:
        for i in range(steps_per_revolution):
            # Step the motor
            GPIO.output(step_pin, GPIO.HIGH)
            time.sleep(0.01)  # delay in seconds
            GPIO.output(step_pin, GPIO.LOW)
            time.sleep(0.01)  # delay in seconds
        time.sleep(1)  # wait for 1 second between revolutions

except KeyboardInterrupt:
    GPIO.cleanup()
