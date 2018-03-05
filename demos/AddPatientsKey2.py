#!/usr/bin/env python
# title           :AddPatientsKey2.py
# description     :Create Sample Data for Patients,Consultations,Prescriptions
# author          :Franco.Ucci
# date            :25-Jun-2017
# version         :2.1
# usage           :python3 AddPatientsKey2.py
# notes           :
# python_version  :3.x
# ==============================================================================

import requests
import json
import pprint
import datetime
import random
from datetime import timedelta

api_url ="http://dev-apis.oracleau.cloud:3006/"
carer_id =""
patient_id =""

patient1 = {
 "Patients": [

    {
      "FullName": "Laura Perez",
      "Age": "54",
      "Address": "35 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "61558755883",
      "Email": "laura.perez@gmail.com",
      "ContactMethod": "SMS",
      "CarerId": "593d429079a2092b58a5218c"
    },]}

patient_group = {
    "Patients": [

        {
      "FullName": "John Perez",
      "Age": "65",
      "Address": "35 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "0421886162",
      "Email": "john.perez@gmail",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    },
    {
      "FullName": "Shane Ross",
      "Age": "91",
      "Address": "42 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "0424604578",
      "Email": "shane.ross@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    },
    {
      "FullName": "Rachel Shea",
      "Age": "82",
      "Address": "44 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "046437353",
      "Email": "rachel.shea@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    },
    {
      "FullName": "Kelly Shea",
      "Age": "85",
      "Address": "44 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "0419762881",
      "Email": "kelly.shea@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    }
  ]
}

resp = requests.post(api_url+'patients', data=json.dumps(patient1),  headers={'Content-Type':'application/json'},)
if resp.status_code != 200:
    raise ApiError('POST /patient/ {}'.format(resp.status_code))

patient1_record = resp.json()

print ("1st Patient Record")
print (patient1_record)
print (patient1_record['Patients'][0]["Email"])
print (patient1_record['Patients'][0]["_id"])
carer_id = patient1_record['Patients'][0]["_id"]
print ("End of 1st Patient Record")

patient_group["Patients"][0]["CarerId"]=carer_id
patient_group["Patients"][1]["CarerId"]=carer_id
patient_group["Patients"][2]["CarerId"]=carer_id
patient_group["Patients"][3]["CarerId"]=carer_id

# print (patient_group)

resp = requests.post(api_url+'patients', data=json.dumps(patient_group),  headers={'Content-Type':'application/json'},)
if resp.status_code != 200:
    raise ApiError('POST /patient/ {}'.format(resp.status_code))

patientgroup_record = resp.json()

print ("Group Patients")
print (patientgroup_record)

VisitReason_Set = ['Cough','Cough','Cough','Cough','Headache','Headache','Headache','Headache','Rash','Rash','Rash','Rash',  ]
SubjectiveNote_Set = ['Hard to Breathe','Thick Yellow Flem','Needs to Rest','Antibiotics Needed','Not Sleeping','Strong Pain with Light and Sound','DeHydrated','Stomach Issues with Headache','On Arms','Between Legs','On the Face','On the Tummy']
Diagnosis_Set = ['Pneumonia', 'Chest Infection', 'Fluid on the Lungs', 'Broncitis', 'Insomnia','Migraine','Needs to Drink More Water', 'Food Poisoning','Cream Allegy','Use Cream for Running','Food Allegy','Stomach Issue']

Consult= {
  "MedicalConsultations": [
    {
      "VisitReason": "Severe cough",
      "ConsultationDate": "2017-05-22T09:00:00",
      "SubjectiveNote": "Patient complained about chest pain",
      "Diagnosis": "Chest infection",
      "PatientId": ""
    }
  ]
}
print (patientgroup_record["Patients"][0]["_id"])
print (patientgroup_record["Patients"][1]["_id"])
print (patientgroup_record["Patients"][2]["_id"])
print (patientgroup_record["Patients"][3]["_id"])

for index in range(0,4,1):

    VT=random.randrange(12)
    pid=patientgroup_record["Patients"][index]["_id"]
    Consult["MedicalConsultations"][0]["VisitReason"]=VisitReason_Set[VT]
    Consult["MedicalConsultations"][0]["ConsultationDate"]=(datetime.datetime.today() - timedelta(days=random.randrange(50))).isoformat()
    Consult["MedicalConsultations"][0]["SubjectiveNote"]=SubjectiveNote_Set[VT]
    Consult["MedicalConsultations"][0]["Diagnosis"]=Diagnosis_Set[VT]
    Consult["MedicalConsultations"][0]["PatientId"]=pid
    resp = requests.post(api_url+'patient/'+pid+'/consultations', data=json.dumps(Consult),  headers={'Content-Type':'application/json'},)

    if resp.status_code != 200:
        raise ApiError('POST /patient/ {}'.format(resp.status_code))

    print ('Here is Consult')
    print (Consult)
    print (resp.json())

    VT=random.randrange(12)
    pid=patientgroup_record["Patients"][index]["_id"]
    Consult["MedicalConsultations"][0]["VisitReason"]=VisitReason_Set[VT]
    Consult["MedicalConsultations"][0]["ConsultationDate"]=(datetime.datetime.today() - timedelta(days=random.randrange(50))).isoformat()
    Consult["MedicalConsultations"][0]["SubjectiveNote"]=SubjectiveNote_Set[VT]
    Consult["MedicalConsultations"][0]["Diagnosis"]=Diagnosis_Set[VT]
    Consult["MedicalConsultations"][0]["PatientId"]=pid
    resp = requests.post(api_url+'patient/'+pid+'/consultations', data=json.dumps(Consult),  headers={'Content-Type':'application/json'},)

    if resp.status_code != 200:
        raise ApiError('POST /patient/ {}'.format(resp.status_code))

    print ('Here is Consult')
    print (Consult)
    print (resp.json())

