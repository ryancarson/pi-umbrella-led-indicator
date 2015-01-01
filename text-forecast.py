import requests

key = '1676775e3b48f757'
api_url = 'http://api.wunderground.com/api/' + key + '/forecast/q/OR/Portland.json'

r = requests.get(api_url)
forecast = r.json
print(forecast['forecast']['txt_forecast']['forecastday'][0]['fcttext'])
