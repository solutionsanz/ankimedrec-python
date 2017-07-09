#!/usr/bin/env python
# title           :01_basic_get_physicians.py
# description     :Uses the Physicians Medrec REST API to return list of physicians
# author          :Jason.Lowe
# date            :05-Jul-2017
# version         :3.0
# usage           :py 01_basic_get_physicians.py
# notes           :Uses API Platform with API Key to interact with REST API which is being managed by API Platform
# python_version  :3.x
# ==============================================================================

import requests
import json
import pprint

# set use_code_url to True to use #OracleCode hosted environment
# set use_code_url to False to use locally hosted environment
# set code_api_key to application key provided by API Platform Cloud Service (if None it will default to locally hosted environment)
use_code_url = False
code_api_url = 'https://apip.oracleau.cloud/api/medrec'
code_apikey_key = 'X-App-Key'
code_apikey_value = ''

# locally hosted environment URL
local_api_url = "http://localhost:3000"

headers = {}

class APIError(Exception):
  """An API Error Exception"""

  def __init__(self, status):
    self.status = status

  def __str__(self):
    return "APIError: status={}".format(self.status)

# Some basic logic to help the transition from local environment to OracleCode environment
if use_code_url and code_apikey_value != '':
  api_url = code_api_url
  if code_apikey_key:
    headers.update({code_apikey_key: code_apikey_value})
else:
  api_url = local_api_url

resp = requests.get(api_url+'/physicians', headers=headers)
if resp.status_code != 200:
    # This means something went wrong.
    raise APIError('GET /physicians/ {}'.format(resp.status_code))

pprint.pprint (resp.json())
