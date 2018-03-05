#!/usr/bin/env python
# title           :MySecondPyhton.py
# description     :Uses the Physicians Medrec REST API to create a new Physican Entry
# author          :Franco.Ucci
# date            :25-Jun-2017
# version         :2.1
# usage           :python3 MyFirstPython.py
# notes           :Uses API Platform with API Key to interact with REST API which is being managed by API Platform
# python_version  :3.x
# ==============================================================================

import requests
import json
import pprint

physician = {
  "Physicians": [
    {
      "FullName": "Patrick Gauci",
      "MedicalSpeciality": "Aged Care"
    }
  ]
}

api_url ="http://dev-apis.oracleau.cloud:3006/"

resp = requests.post(api_url+'physicians', data=json.dumps(physician),  headers={'App-key':'a6285f57-0aea-4925-88ca-fa21f78d645d'} ,)
if resp.status_code != 200:
    raise ApiError('POST /physicians/ {}'.format(resp.status_code))
print('Created Physician', json.dumps(physician))
