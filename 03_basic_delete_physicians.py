#!/usr/bin/env python
# title           :03_basic_delete_physicians.py
# description     :Uses the Physicians Medrec REST API to delete Physicans Entries until 4 Physicians are left
# author          :Jason.Lowe
# date            :05-Jul-2017
# version         :3.0
# usage           :py 03_basic_delete_physicians.py
# notes           :Uses API Platform with API Key to interact with REST API which is being managed by API Platform
# python_version  :3.x
# ==============================================================================

import requests

physician_list = []
physician_no = 0

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
  print('OracleCode hosted environment exclude this functionality')
  exit()
  # api_url = code_api_url
  # if code_apikey_key:
  #   headers.update({code_apikey_key: code_apikey_value})
else:
  api_url = local_api_url

r = requests.get(api_url+'/physicians', headers=headers)

j = r.json()

print (j['Physicians'])
for each in j['Physicians']:
    physician_no = physician_no +1
    print (physician_no)
    print (each['_id'])
    physician_list.append(each ['_id'])

print ('We have following No of Physicians ', physician_no)
print ('+++++++++++++++++++++++++++++++++')
print ('deleting excess physicians, leaving 4 physicians in the database')

for i in range (4, physician_no, 1):
    print ('physician ',i,' with id ',physician_list[i])
    print (api_url+'/physicians/'+physician_list[i])
    resp = requests.delete(api_url+'/physicians/'+physician_list[i], headers=headers)
    print ('Response Code ', resp)
