import requests
import json

url = "http://127.0.0.1:8000/predict-fraud"
# step: List[int]
#     type: List[str]
#     amount: List[float]
#     nameOrig:  List[str]
#     oldbalanceOrig: List[float]
#     newbalanceOrig: List[float]
#     nameDest:  List[str]
#     oldbalanceDest: List[float]
#     newbalanceDest: List[float]

# payload = json.dumps({
#   "step": 0,
#   "type": 'PAYMENT',
#   "amount": 0.323318405,
#   "nameOrig": 'C1231006815',
#   "oldbalanceOrig": 0.0856723112,
#   "newbalanceOrig": 0.0306624283,
#   "nameDest": "M1979787155",
#   "oldbalanceDest": 0.443876228,
#   "newbalanceDest": 0.443876228

# })
payload = json.dumps(
{
  "step": [
    0
  ],
  "type": [
    "PAYMENT"
  ],
  "amount": [
    0
  ],
  "nameOrig": [
    "C1231006815"
  ],
  "oldbalanceOrig": [
    0
  ],
  "newbalanceOrig": [
    0
  ],
  "nameDest": [
    "M1979787155"
  ],
  "oldbalanceDest": [
    0
  ],
  "newbalanceDest": [
    0
  ]
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)