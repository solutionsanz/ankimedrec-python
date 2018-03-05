import requests
import json
import pprint

Patient_No = 20



patient = {
 "Patients": [

    {
      "FullName": "Laura Perez",
      "Age": "25",
      "Address": "35 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "61558755883",
      "Email": "laura.perez@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d429079a2092b58a5218c"
    },
    {
      "FullName": "John Perez",
      "Age": "35",
      "Address": "35 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "0421886162",
      "Email": "john.perez@gmail",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    },
    {
      "FullName": "Shane Ross",
      "Age": "61",
      "Address": "42 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "0424604578",
      "Email": "shane.ross@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    },
    {
      "FullName": "Rachel Shea",
      "Age": "42",
      "Address": "44 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "046437353",
      "Email": "rachel.shea@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    },
    {
      "FullName": "Kelly Shea",
      "Age": "52",
      "Address": "44 Napier St, 3065, Fitzroy, VIC, Australia",
      "Mobile": "0419762881",
      "Email": "kelly.shea@gmail.com",
      "ContactMethod": "Carer",
      "CarerId": "593d2495c6d353283335b49b"
    }
  ]
}

resp = requests.post('http://dev-apis.oracleau.cloud:3006/patients', data=json.dumps(patient),  headers={'Content-Type':'application/json'},)
if resp.status_code != 200:
    raise ApiError('POST /patient/ {}'.format(resp.status_code))
print('Created Patients', json.dumps(patient))



