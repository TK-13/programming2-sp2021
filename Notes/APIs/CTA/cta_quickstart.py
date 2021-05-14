# https://www.transitchicago.com/developers/
# https://www.transitchicago.com/assets/1/6/cta_Customer_Alerts_API_Developer_Guide_and_Documentation_20160929.pdf

print("\n\n------------------------------------------------------------------------------\n\n")
print("Testing Customer Alerts API\n\n")

import requests

routes = ['red', 'blue', 'brn', 'g', 'org', 'p', 'pexp', 'pink', 'y']

for route in routes:
    result = requests.get('http://www.transitchicago.com/api/1.0/routes.aspx?routeid=' + route + '&outputType=JSON')
    routeInfo = result.json()['CTARoutes']['RouteInfo']
    print(routeInfo['Route'] + ': ' + routeInfo['RouteStatus'])

print("\n\n------------------------------------------------------------------------------\n\n")


# https://www.transitchicago.com/developers/bustracker/
# Bus Tracker

print("Testing Bus Tracker API\n\n")

import requests
from datetime import datetime

key = 'YyTJVHZBw3mhgCntC9QVQSFFc'
stop = '1333'

result = requests.get('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=' + key + '&stpid=' + stop + '&format=json')
etas = result.json()['bustime-response']['prd']
if etas:
    print(etas[0]['stpnm'] + ' (' + etas[0]['rtdir'] + ')\n')
for eta in etas:
    print('Predicted minutes remaining until arrival: ' + eta['prdctdn'])
    print('Predicted arrival time: ' + datetime.strptime(eta['prdtm'].split(' ')[-1], '%H:%M').strftime('%I:%M %p'))
    print()


print("------------------------------------------------------------------------------\n\n")



# https://www.transitchicago.com/developers/ttdocs/
# Train Tracker

print("Testing Train Tracker API\n\n")

import requests
from datetime import datetime

key = '3a88c0db3ae74b929f650234254fc4a5'
stop = '40570'
result = requests.get('http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=' + key + '&mapid=' + stop + '&outputType=JSON')
etas = result.json()['ctatt']['eta']
if etas:
    print(etas[0]['staNm'] + ' ' + etas[0]['rt'] + ' Line Stop\n')
for eta in etas:
    print(eta['stpDe'] + ': ' + datetime.strptime(eta['arrT'], '%Y-%m-%dT%H:%M:%S').strftime('%I:%M:%S %p (%m-%d-%y)'))

print("------------------------------------------------------------------------------\n\n")