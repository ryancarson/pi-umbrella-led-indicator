import requests
import RPi.GPIO as GPIO
import time

'''
To learn how to wire up LEDs on a Raspberry Pi, check out 
http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html
'''

red_led = 17
green_led = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

# Grab your own API Key at wunderground.com with a free account. Don't abuse mine :)
api_key = '1676775e3b48f757'

# Change this URL to match your location
api_url = 'http://api.wunderground.com/api/' + api_key + '/forecast/q/OR/Portland.json'

# Used to get the pop value for a specified day. 0 is today 
day = 0

while True:
	request = requests.get(api_url)
	forecast = request.json
	
	# pop_value is the 'probability of precipitation'
	pop_value = forecast['forecast']['txt_forecast']['forecastday'][day]['pop']
	pop_value = int(pop_value)
	
	if pop_value >= 30:
		GPIO.output(red_led, GPIO.HIGH)
		GPIO.output(green_led, GPIO.LOW)
	else:
		GPIO.output(green_led, GPIO.HIGH)
		GPIO.output(red_led, GPIO.LOW)
	time.sleep(180)
