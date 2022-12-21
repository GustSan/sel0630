from requests import get
import json
from pprint import pprint

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

weather = weather + str(966583)

my_weather = get(weather).json()['items']
pprint(my_weather)
