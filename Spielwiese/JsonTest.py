#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import json
import urllib

jsonstr = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?q=WIEN,it&units=metric&lang=&lang=de&APPID=dd54446e9ff8c59e593931edfbdd6437').read()
j = json.loads(jsonstr)

#print j
#print j['coord']
#print j['sys']
print j ['weather'][0]['description']
#print j['base']
print j['main']['temp']
print j['wind']['speed']
#print j['rain']
#print j['clouds']
#print j['dt']
#print j['id']
print j['name']
#print j['cod']


# {
# "coord":{"lon":16.37,"lat":48.21},
# "sys":{"message":0.0091,"country":"AT","sunrise":1390717769,"sunset":1390751087},
# "weather":[{"id":600,"main":"Snow","description":"mäßiger Schnee","icon":"13n"}],
# "base":"cmc stations",
# "main":{"temp":-4,"humidity":51,"pressure":1012.4,"temp_min":-7.6,"temp_max":-0.56},
# "wind":{"speed":1.5,"deg":135.5},
# "snow":{"3h":0.75},
# "clouds":{"all":92},
# "dt":1390761253,
# "id":2761369,
# "name":"Vienna",
# "cod":200
# }

# json_input = '{ "one": 1, "two": { "list": [ {"item":"A"},{"item":"B"} ] } }'

