import requests

api_url ="http://dev-apis.oracleau.cloud:3006/"


resp = requests.delete(api_url+'collection/patients')
print ("Response Code ", resp)
print ("Just deleted Patients.")

resp = requests.delete(api_url+'collection/consultations')
print ("Response Code ", resp)
print ("Just deleted Consultations")

resp = requests.delete(api_url+'collection/prescriptions')
print ("Response Code ", resp)
print ("Just deleted Prescriptions.")

resp = requests.delete(api_url+'collection/observations')
print ("Response Code ", resp)
print ("Just deleted Observations.")

