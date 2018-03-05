import datetime
import random
import requests
import json
import numpy as np

NoObs=10
today = datetime.datetime.today()
# one_day = datetime.timedelta(days=1)
one_hour = datetime.timedelta(hours=1)

patient_id = '593d249ec6d353283335b49c'

systolic, diatonic, heart, weight, hi_sigma, lo_sigma = 160, 100, 90, 80, 20, 3

systolic_list = np.random.normal(systolic, hi_sigma, NoObs)
diatonic_list = np.random.normal(diatonic, hi_sigma, NoObs)
heart_list = np.random.normal(heart, lo_sigma, NoObs)
weight_list = np.random.normal(weight, lo_sigma, NoObs)

for i in range (1,NoObs,1):
    ODate = today - (one_hour * i)
    post_url = 'http://dev-apis.oracleau.cloud:3006/patient/' + patient_id + '/observations'
    obs_short = '{"MedicalObservations": [{"Name": "Weight","Unit": "kg", "Value": "'+str(int(weight_list[i]))+'","Producer": "Self","RecordingDevice": "Self","Date": "'+str(ODate.isoformat())+'","Notes": "Auto Generated","PatientId": "'+patient_id+'"}]}'
    resp = requests.post(url=post_url, data=obs_short, headers={'Content-Type':'application/json'},)
    obs_short = '{"MedicalObservations": [{"Name": "Heart","Unit": "bpm", "Value": "'+str(int(heart_list[i]))+'","Producer": "Self","RecordingDevice": "Self","Date": "'+str(ODate.isoformat())+'","Notes": "Auto Generated","PatientId": "'+patient_id+'"}]}'
    resp = requests.post(url=post_url, data=obs_short, headers={'Content-Type':'application/json'},)
    obs_short = '{"MedicalObservations": [{"Name": "Systolic","Unit": "systolic", "Value": "' + str(int(systolic_list[i])) + '","Producer": "Self","RecordingDevice": "Self","Date": "' + str(ODate.isoformat()) + '","Notes": "Auto Generated","PatientId": "' + patient_id + '"}]}'
    resp = requests.post(url=post_url, data=obs_short, headers={'Content-Type': 'application/json'}, )
    obs_short = '{"MedicalObservations": [{"Name": "Diatonic","Unit": "diatonic", "Value": "' + str(int(diatonic_list[i])) + '","Producer": "Self","RecordingDevice": "Self","Date": "' + str(ODate.isoformat()) + '","Notes": "Auto Generated","PatientId": "' + patient_id + '"}]}'
    resp = requests.post(url=post_url, data=obs_short, headers={'Content-Type': 'application/json'}, )

#    print(obs_short)
#    print (resp.status_code)

#if resp.status_code != 200:
#    raise ApiError('POST /Patient Observations/ {}'.format(resp.status_code))

#    print (OName, ' ', OUnit,' ', OWeight,' ',OHeart,' ',OSystolic,' ',ODiatonic,' ',OProducer,' ',ODate.isoformat())

