import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 23; echo = 24; red = 18

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
red_pwm = GPIO.PWM(red, 100)

GPIO.output(trig, False)
time.sleep(2)

try:
    while True:

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        tim_start = time.time()
        time_end = time.time()

        while (GPIO.input(echo) == 0):
            tim_start = time.time()

        while (GPIO.input(echo) == 1):
            time_end = time.time()

        timeTaken = time_end - tim_start
        distance = (timeTaken*34300)/2

        if (distance > 200):
            print("Distance is beyond limit")

        elif (distance > 50):
            red_pwm.ChangeDutyCycle(0)
            print("Distance -> ", distance, "cm ; LED value -> ",(100 - (distance_in_cm*2)))

        else:
            red_pwm.ChangeDutyCycle(100 - (distance_in_cm*2))
            print("Distance -> ", distance, "cm ; LED value -> ",(100 - (distance_in_cm*2)))

            distance_in_cm = distance

        time.sleep(1)

except:
    print("An error has occured.")

finally:
    GPIO.cleanup()
