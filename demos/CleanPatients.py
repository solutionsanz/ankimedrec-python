import requests

patient_list = []
patient_no = 0

# r = requests.get('http://api.zippopotam.us/us/ma/belmont')

r = requests.get('http://dev-apis.oracleau.cloud:3006/patients')

j = r.json()

print (j['Patients'])
for each in j['Patients']:
    patient_no = patient_no +1
    print (patient_no)
    print (each['_id'])
    patient_list.append(each ['_id'])

print ("We have following No of Patients ", patient_no)
print ("+++++++++++++++++++++++++++++++++ ")
print ("delete time, leaving 5 patients ")

for i in range (2, patient_no, 1):
    print ("patient ",i," with id ",patient_list[i])
    print ("http://dev-apis.oracleau.cloud:3006/patients/"+patient_list[i])
    resp = requests.delete('http://dev-apis.oracleau.cloud:3006/patient/'+patient_list[i])
    print ("Response Code ", resp)
