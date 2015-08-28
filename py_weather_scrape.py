import requests
import urllib2
import json
import serial

# serial setup for ze arduino
#s = serial.Serial(port='/dev/tty.usbmodem1421', baudrate=9600)

can_city = str(raw_input("Enter A Canadian City > "))

url_f = 'http://api.wunderground.com/api/66fc49ad8e8c31b8/geolookup/conditions/q/Canada/%s.json' % can_city
url_r = 'http://api.wunderground.com/api/66fc49ad8e8c31b8/forecast/q/Canada/%s.json' % can_city

f = urllib2.urlopen(url_f) 
json_string = f.read() 

parsed_json = json.loads(json_string) 
location = parsed_json['location']['city']
country = parsed_json['location']['country'] 

r = requests.get(url_r)
data = r.json()

print "----------------------------"
print "Forecast for: %s, %s" % (location, country)
print "----------------------------"



for day in data['forecast']['simpleforecast']['forecastday']:
	print day['date']['weekday'] + ": "
	print "Conditions: ", day['conditions']
	print "High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius']
	print "P.O.P: ", day['pop'] 
	
	# cram the POP into a variable
	pop = day['pop']

	if pop in range(0,40):
		print "not gonna rain"
		#s.write(str('s'));
	elif pop in range(41,60):
		print "might rain"
		#s.write(str('m'));
	elif pop in range(61,100):
		print "TOTES RAIN YO"
		#s.write(str('r'));
	else: 
		print "meh"
	

	print "----------------------------"

#do this by POP
# I'd like make an arduino display that shows if it is sunny in the forecast or not. 
# I would like this also hooked up to a local server.