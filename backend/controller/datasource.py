from flask_restful import Resource
from domain import HydroPower
import urllib.request
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

class Datasource:
    base_url = "https://sitr.cnd.com.pa"
    
    def get_data():    
        response = requests.get("https://sitr.cnd.com.pa/m/pub/data/gen.json?1683852530787", timeout=30)
        if(response.status_code == 200):
            return response.json()
        else:
            logging.error("Error: %s", response.status_code)
    
    def get_plants():    
        response = requests.get("https://sitr.cnd.com.pa/m/pub/data/vert.json?1683859684699", timeout=30)
        if(response.status_code == 200):
            return response.json()
        else:
            logging.error("Error: %s", response.status_code)
    
    def get_generation_by_plants():    
        response = requests.get("https://sitr.cnd.com.pa/m/pub/data/vert.json?1683859684699", timeout=30)
        if(response.status_code == 200):
            return response.json()
        else:
            logging.error("Error: %s", response.status_code)

