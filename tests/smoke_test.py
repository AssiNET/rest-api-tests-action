########################
### BUILD-IN IMPORTS ###
import json
import unittest
import logging
import os
import sys
import datetime
import random
import time

#########################
### FRAMEWORK IMPORTS ###
import sys
print(sys.path)
from lib.request_lib import Request
from lib.common_lib import Reporting # Create Reporting shortcut
import lib.common_lib as common_lib
from lib.configman import ConfigMan

##########################
######   SETTINGS   ######
sys.dont_write_bytecode = True # Disable .pyc file generation
logging.basicConfig(format='%(message)s',level=logging.INFO)

##################################################
#### HOW TO RUN/DEBUG THIS TEST SET ##############
##################################################
### 1. Open .vscode/launch.json                 ##
### 2. Update config name 'Tests' with set name ##
### 3. From sidebar open 'Run and Debug' tab    ##
### 4. Select 'Tests Run/Debug' from dropdown   ##
##################################################

###########################
#### GLOBAL CONSTANTS  ####
ConfigMan.DEFAULT_RESPONSE_TIME = 5
ConfigMan.BACKEND_URL = "https://ssd-api.jpl.nasa.gov/cad.api"

###########################
#### GLOBAL VARIABLES  ####
timestamp = str(datetime.datetime.now().strftime("_%Y_%m_%d_%H_%M_%S"))
timestamp_time = str(datetime.datetime.now().strftime("%H_%M_%S"))

class SmokeTests(unittest.TestCase):

    def test_100_Verify_Close_Approach_Data(self):
        headers = {
            'user-agent': 'Chrome/109.0.0.0',
            'content-type': 'application/json',
            'accept': '*/*'
        }

        params = {
            'des': "433",
            'date-min': "1900-01-01",
            'date-max': '2100-01-01',
            'dist-max': '0.2'
        }

        url = ConfigMan.BACKEND_URL
        response, content = Request.GET(url, headers, params=params)
        ###############################
        assert (response.status_code == 200)
        assert (response.elapsed.total_seconds() < ConfigMan.DEFAULT_RESPONSE_TIME)

        body_json = response.json()
        assert body_json["count"] == "5"
        assert body_json["signature"]["source"] == "NASA/JPL SBDB Close Approach Data API"
        assert len(body_json["fields"]) == 11

    def test_150_Verify_Close_Approach_Data_Sorted_by_Distance(self):
        headers = {
            'user-agent': 'Chrome/109.0.0.0',
            'content-type': 'application/json',
            'accept': '*/*'
        }

        params = {
            'dist-max': "10LD",
            'date-min': "2018-01-01",
            'sort': "dist",
        }

        url = ConfigMan.BACKEND_URL
        response, content = Request.GET(url, headers, params=params)
        ###############################
        assert (response.status_code == 200)
        assert (response.elapsed.total_seconds() < 10)

        body_json = response.json()
        assert body_json["count"] == "4313"

        #TODO
        #assert dist is ordered
        #assert min year in each item at least 2018 - check all items

    def test_200_Verify_Status_Code_400(self):
        headers = {
            'user-agent': 'Chrome/109.0.0.0',
            'content-type': 'application/json',
            'accept': '*/*'
        }

        params = {
            'WRONG': "WRONG",
            'date-min': "1900-01-01",
            'date-max': 'WRONG',
            'dist-max': '0.2'
        }

        url = ConfigMan.BACKEND_URL
        response, content = Request.GET(url, headers, params=params)
        ###############################
        assert (response.status_code == 400)
        assert (response.elapsed.total_seconds() < ConfigMan.DEFAULT_RESPONSE_TIME)

    def test_300_Verify_Status_Code_405(self):
        headers = {
            'user-agent': 'Chrome/109.0.0.0',
            'content-type': 'application/json',
            'accept': '*/*'
        }

        params = {
            'des': "433",
            'date-min': "1900-01-01",
            'date-max': '2100-01-01',
            'dist-max': '0.2'
        }

        url = ConfigMan.BACKEND_URL
        response, content = Request.DELETE(url, headers, params=params)
        ###############################
        assert (response.status_code == 405)
        assert (response.elapsed.total_seconds() < ConfigMan.DEFAULT_RESPONSE_TIME)

if __name__ == '__main__':
    unittest.main()
