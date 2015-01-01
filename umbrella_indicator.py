import requests
import RPi.GPIO as GPIO
import time

red_led = 17
green_led = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

api_key = '1676775e3b48f757'
api_url = 'http://api.wunderground.com/api/' + api_key + '/forecast/q/OR/Portland.json'

while True:
	request = requests.get(api_url)
	forecast = request.json
	pop_value = forecast['forecast']['txt_forecast']['forecastday'][0]['pop']
	pop_value = int(pop_value)

	if pop_value >= 30:
		GPIO.output(red_led, GPIO.HIGH)
		GPIO.output(green_led, GPIO.LOW)
	else:
		GPIO.output(green_led, GPIO.HIGH)
		GPIO.output(red_led, GPIO.LOW)
	time.sleep(180)
