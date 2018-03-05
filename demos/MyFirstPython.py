#!/usr/bin/env python
# title           :MyFirstPyhton.py
# description     :Uses the Physicians Medrec REST API to return list of physicians
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

resp = requests.get('http://apip.oracleau.cloud/api/physicians', headers={'App-key':'a6285f57-0aea-4925-88ca-fa21f78d645d'} )
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /physicians/ {}'.format(resp.status_code))
pprint.pprint (resp.json())

