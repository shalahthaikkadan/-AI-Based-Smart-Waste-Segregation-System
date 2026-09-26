import RPi.GPIO as GPIO
import time

servo_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(servo_pin, GPIO.OUT)

def main():
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(0)
    while True:
        pwm.ChangeDutyCycle(8.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
    pwm.stop()

main()


