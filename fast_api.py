import joblib
import uvicorn
from fastapi import FastAPI,Request
from pydantic import BaseModel
import pandas as pd
import numpy as np
from typing import List

def preprocess(data):
    '''
    objective: preprocess the data to feed into model.
    data: i/p data user entered in the form.

    '''
    scaler=joblib.load("./utils/scale2.joblib", mmap_mode=None)
    le=joblib.load("./utils/le2.joblib", mmap_mode=None)
    data['dif_dest']=data['newbalanceDest']-data['oldbalanceDest']
    data['amount_dif']=data['newbalanceOrig']-data['amount']

    cat_col=['type']
    num_col=['step', 'amount', 'oldbalanceOrig', 'newbalanceOrig', 'oldbalanceDest',
       'newbalanceDest', 'dif_dest', 'amount_dif']
    scale_train=scaler.transform(data[num_col])
    le_train=le.transform(data[cat_col])
    train_X=np.concatenate([le_train,scale_train],axis=1)
    return train_X


class ClientData(BaseModel):
    '''
    json Data i/p for the API call.
    '''
    step: int
    type: str
    amount: float
    nameOrig:  str
    oldbalanceOrig: float
    newbalanceOrig: float
    nameDest:  str
    oldbalanceDest: float
    newbalanceDest: float


app = FastAPI()
@app.get('/')
def get_root():
    return {'message': 'Welcome to the spam detection API'}

@app.post("/is-fraud")
async  def predict_fraud(item :ClientData):
  '''
  objective: final prediction api.
  return: returns isFraud True/False.
  '''
  # Getting the JSON from the body of the request
  h=item.dict()
  df=pd.DataFrame([h])
  #passing it to preprocessing pipeline
  inp=preprocess(df)
  #prediction
  model=joblib.load("./models/model2.joblib", mmap_mode=None)
  pred = model.predict(inp)[0]
  if pred==0:
    return {'isFraud':False}
  else:
    return {'isFraud':True}