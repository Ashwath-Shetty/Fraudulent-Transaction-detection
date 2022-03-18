# from fastapi import FastAPI
import joblib
import uvicorn
from fastapi import FastAPI,Request
from pydantic import BaseModel
import pandas as pd
import numpy as np
#import nest_asyncio
from typing import List

def preprocess(data):
    '''
    objective: preprocess the data to feed into model.
    data: i/p data user entered in the form.

    '''
    scaler=joblib.load("./utils/scale.joblib", mmap_mode=None)
    le=joblib.load("./utils/le.joblib", mmap_mode=None)
    data['dif_dest']=data['newbalanceDest']-data['oldbalanceDest']
    data['amount_dif']=data['newbalanceOrig']-data['amount']

    cat_col=['type', 'nameOrig', 'nameDest']
    num_col=['step', 'amount', 'oldbalanceOrig', 'newbalanceOrig', 'oldbalanceDest',
       'newbalanceDest', 'dif_dest', 'amount_dif']
    print("--pre",data[cat_col])
    scale_train=scaler.transform(data[num_col])
    le_train=le.transform(data[cat_col])
    train_X=np.concatenate([le_train,scale_train],axis=1)
    return train_X

# class ClientData(BaseModel):
#     step: List[int]
#     type: List[str]
#     amount: List[float]
#     nameOrig:  List[str]
#     oldbalanceOrig: List[float]
#     newbalanceOrig: List[float]
#     nameDest:  List[str]
#     oldbalanceDest: List[float]
#     newbalanceDest: List[float]

class ClientData(BaseModel):
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

@app.get('/ping')
def ping():
  '''
  This is a first docstring.
  '''
  return ('pong', 200)


# @app.post('/basic_predict')
# async def basic_predict(request: Request):
#   '''
#   This is a first docstring.
#   '''
#   # Getting the JSON from the body of the request
#   input_data = await request.json()

#     # Converting JSON to Pandas DataFrame
#   input_df = pd.DataFrame([input_data])
#   model=joblib.load("./models/model.joblib", mmap_mode=None)
#   # Getting the prediction 
#   pred = model.predict(input_df)[0]

#   return pred


@app.post("/predict-fraud")
async  def predict_fraud(item :ClientData):
  '''
  This is a first docstring.
  '''
  # Getting the JSON from the body of the request
  # input_data = await request.json()
  # print("------",input_data)

  #   # Converting JSON to Pandas DataFrame
  # input_df = pd.DataFrame([input_data])
  h=item.dict()
  # print("fast",fastapi.__version__)
  # print("fast",pydantic.__version__)
  # print("fast",uvicorn.__version__)
  print('---------',h)
  #df=pd.DataFrame.from_dict(h, orient="columns")
  df=pd.DataFrame([h])
  print("------------->",df.head())
  inp=preprocess(df)
  
  model=joblib.load("./models/model.joblib", mmap_mode=None)
  # Getting the prediction 
  pred = model.predict(inp)[0]
  print(pred)
  if pred==0:
    return {'Fraud':False}
  else:
    return {'Fraud':True}

  #return pred