from unicodedata import name
import config
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import ExtraTreesClassifier
import joblib

def create_train_test_data(dataset):
    '''
    objective: creates train and test dataset and saves under data folder for further steps.
    dataset: complete dataset to create train and test.

    '''
    # load and split the data
    X = dataset.drop(['isFraud'], axis=1)
    Y = dataset['isFraud']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42,stratify=Y)

    data_train = pd.concat([X_train,y_train],axis=1)
    data_test = pd.concat([X_test,y_test],axis=1)
    # save the data
    data_train.to_csv('../data/train.csv', index=False)
    data_test.to_csv('../data/test.csv', index=False)
    print(f"Train data for modeling: {data_train.shape}")
    print(f"Test data for predictions: {data_test.shape}")
    
    return "train and test files are created under data folder"

def preprocess(train,test):
    '''
    objective: preprocess the train and test datasets and prepares the data for modeling. 
    train: train datasets.
    test: test datasets.
    returns: train_X,y_train,test_X,y_test

    '''
    #feature engineering
    train['dif_dest']=train['newbalanceDest']-train['oldbalanceDest']
    train['amount_dif']=train['newbalanceOrig']-train['amount']
    test['dif_dest']=test['newbalanceDest']-test['oldbalanceDest']
    test['amount_dif']=test['newbalanceOrig']-test['amount']
    #cat and num col extractor
    num_col=train.drop(['isFraud'], axis=1).select_dtypes(include=['int64','float64']).columns
    cat_col= train.drop(['isFraud'], axis=1).select_dtypes(exclude=['int64','float64']).columns
    # encoding
    le=preprocessing.OrdinalEncoder()
    scaler=preprocessing.QuantileTransformer()
    concatinated=pd.concat([train[cat_col],test[cat_col]])
    le.fit(concatinated)
    le_train=le.transform(train[cat_col])
    le_test=le.transform(test[cat_col])

    scaler.fit(train[num_col])
    scale_train=scaler.transform(train[num_col])
    scale_test=scaler.transform(test[num_col])
    train_X=np.concatenate([le_train,scale_train],axis=1)
    test_X=np.concatenate([le_test,scale_test],axis=1)
    y_train=train['isFraud'].values
    y_test=test['isFraud'].values
    return train_X,y_train,test_X,y_test

def score(y_true,y_pred):
    '''
    objective: calcualtes the roc_auc score.
    y_true: true labels.
    y_pred: predicted labels.
    
    '''
    #score= 100* (f1_score(y_true,y_pred,average='micro'))
    score=roc_auc_score(y_true,y_pred)
    return score

def export_model(model):
    '''
    objective: saves the model.
    model: model to be saved.
    
    '''
    joblib_path = '../models/model.joblib'
    with open(joblib_path, 'wb') as file:
        joblib.dump(model, file)
        print(f"Model saved at {joblib_path}")

def main():
    #load the whole data
    data = pd.read_csv(config.training_file)
  
    # Split train/test
    # Creates train.csv and test.csv
    create_train_test_data(data)
    # Loads the data for the model training
    train = pd.read_csv('../data/train.csv', keep_default_na=False)
    test = pd.read_csv('../data/test.csv', keep_default_na=False)
    #preprocessing, model training and score calculation
    X_train,y_train,X_test,y_test=preprocess(train,test)
    model=ExtraTreesClassifier(random_state=42,n_jobs=-1)
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    roc_auc=score(X_test,y_test)
    print("roc-auc of test set is",roc_auc)
    #exports the model
    export_model(model)

if __name__ == "__main__":
    main()
