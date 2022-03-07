import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title('Fraudulent Transaction detection')

def preprocess(data):
    '''
    objective: preprocess the data to feed into model.
    data: i/p data user entered in the form.

    '''
    scaler=joblib.load("./utils/scale.joblib", mmap_mode=None)
    le=joblib.load("./utils/le.joblib", mmap_mode=None)
    data['dif_dest']=data['newbalanceDest']-data['oldbalanceDest']
    data['amount_dif']=data['newbalanceOrig']-data['amount']
    data['dif_dest']=data['newbalanceDest']-data['oldbalanceDest']
    data['amount_dif']=data['newbalanceOrig']-data['amount']

    cat_col=['type', 'nameOrig', 'nameDest']
    num_col=['step', 'amount', 'oldbalanceOrig', 'newbalanceOrig', 'oldbalanceDest',
       'newbalanceDest', 'dif_dest', 'amount_dif']
    scale_train=scaler.transform(data[num_col])
    le_train=le.transform(data[cat_col])
    train_X=np.concatenate([le_train,scale_train],axis=1)
    return train_X

def main():
    # UI form to take i/p from users.
    step=st.number_input("Enter the steps",key='1')
    type=st.selectbox('Select the type of transaction',['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
    amount=st.number_input("Enter the amount",min_value=None,value=29,key='2')
    nameOrig= st.text_input("Enter the name orig",help="Enter the name of the customer who started the transcation")
    oldbalanceOrig= st.number_input("Enter the old balance of orig",help="initial balance before the transcation")
    newbalanceOrig= st.number_input("Enter the new balance of orig",help="balance after the transcation")
    nameDest= st.text_input("Enter the name Dest",help="recipient ID of the transaction")
    oldbalanceDest= st.number_input("Enter the old balance of Dest",help="initial reciepient balance before the transcation")
    newbalanceDest= st.number_input("Enter the new balance of Dest",help="reciepient's balance after the transcation")
    values=[[step,type,amount,nameOrig,oldbalanceOrig,newbalanceOrig,nameDest,oldbalanceDest,newbalanceDest]]
    cols=['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrig',
       'newbalanceOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest']
    df=pd.DataFrame(values,columns=cols)
    # saved model loading for prediction
    model=joblib.load("./models/model.joblib", mmap_mode=None)
    # preprocessing and prediction
    if (st.button('predict')):
        final_df=preprocess(df)
        result=model.predict(final_df)
        st.write("result is ",result[0])

if __name__=='__main__':
    main()










