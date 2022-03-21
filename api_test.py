import requests
import json
import requests

'''
objective: to test the api.
'''
url = "https://fraud-t-detection.herokuapp.com/is-fraud"  #to test in production.
#url='http://127.0.0.1:8000/is-fraud'  #-- to test in local host
r = requests.post(url, 
json = {
"step":5,
"type":"PAYMENT",
"amount":9839.64,
"nameOrig":"C1231006815",
"oldbalanceOrig":170136.0,
"newbalanceOrig":160296.36,
"nameDest":"M1979787155",
"oldbalanceDest":0.0,
"newbalanceDest":0.0
})


print("------",r)
print("------",r.text)