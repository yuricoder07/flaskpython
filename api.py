from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_jokes import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/jokes')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)



def getTimezones():
    req = requests.get("https://worldtimeapi.org/api/timezone")
    return(req.text)



# building RESTapi resources/interfaces, these routes are added to Web Server
api.add_resource(getTimezones(), '/create/<string:joke>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://time.nighthawkcodingteams.cf' # run from web
    url = server + "/api/jokes"
    responses = []  # responses list
