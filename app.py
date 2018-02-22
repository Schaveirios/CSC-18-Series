import urllib
import request
import json


#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
#API_KEY
api_key = 'AIzaSyDZNtxwEromEvsPiGFfg7CtektMYt4rj54'

origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')

#Handling request-response 
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()

directions = json.loads(response)

print(directions)