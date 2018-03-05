# -*- encoding: utf-8 -*-

import requests
import json
import pprint
import random

from faker import Factory
fake = Factory.create('en_AU')

Patient_No = 5
for i in range(0,Patient_No):
    # patient_data = '{"FullName":"'+fake.name()+'","Age":"'+'25''+'"Address":"'+fake.address()+'","Mobile":"'+'0415234567'+'","Email":"'+fake.email+'@medrec.com"}'
    # patient_data = '{ "Patients": [{"FullName":"'+fake.name()+'","Age":"'+str(random.randint(20,90))+'","Address":"'+(fake.address()).replace("\n", " ")+'","Mobile":"04'+str(random.randint(4234123,54123456))+'","Email":"'+fake.email()+'"}]}'
    patient_data = '{ "Patients": [{"FullName":"'+fake.name()+'","Age":"'+str(random.randint(20,90))+'","Address":"'+(fake.address()).replace("\n", " ")+'","Mobile":"04'+str(random.randint(4234123,54123456))+'","Email":"'+fake.email()+'"'+',"ContactMethod":"Carer","CarerId":"593d2495c6d353283335b49b"}]}'
    print(patient_data)
    resp = requests.post('http://dev-apis.oracleau.cloud:3006/patients', data=patient_data,  headers={'Content-Type':'application/json'},)
    print ("Patient No "+ str(i) + " with Response Code = "+str(resp.status_code))

if resp.status_code != 200:
  raise ApiError('POST /patient/ {}'.format(resp.status_code))
print('Created Patients')





