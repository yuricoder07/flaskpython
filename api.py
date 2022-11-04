from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_time import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/time')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class timeAPI:
    class _Read(Resource):
        def get(self):
            return jsonify(timeZones())



    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Read, '/')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://time.nighthawkcodingteams.cf' # run from web
    url = server + "/api/timezones"
    responses = []  # responses list

    
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  
        ) 
    responses.append(
        requests.put(url+"/help/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/useless/"+num) # add to jeer count
        ) 

    
    responses.append(
        requests.get(url+"/random")  
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")