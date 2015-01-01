import RPi.GPIO as GPIO

red_led = 17
green_led = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

GPIO.output(red_led, GPIO.LOW)
GPIO.output(green_led, GPIO.LOW)
