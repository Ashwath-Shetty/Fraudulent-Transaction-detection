# Fraudulent-Transaction-Detection
## Live Demo
https://share.streamlit.io/ashwath-shetty/fraudulent-transaction-detection/main/app.py

## Problem Statement
You are provided a synthetic dataset for a mobile payments application. In this dataset, you are
provided the sender and recipient of a transaction as well as whether transactions are tagged as
fraud or not fraud. Your task is to build a fraud detection API that can be called to predict
whether or not a transaction is fraudulent.
You are expected to build a REST API that predicts whether a given transaction is fraudulent or
not. You are also to assume that the previous API calls are to be stored in order to engineer
features relevant to finding fraud. The API calls will include the time step of the transaction, so
you can assume that a transaction happens sequentially within the same time step.

## Folder Structure

    .
    ├── data                     # will have original Data, train and test data files.
    ├── models                   # saved models
    ├── notebooks                # Jupyter notebooks.
    ├── src                     # Source files 
    │    ├── config.py          # configuration files
    │    ├── train.py           # training code
    ├── utils                    # utils for the prediction
    ├── app.py                   # deployed main app code.
    ├── Procfile                 # Procfile incase if you want to deploy to Heroku(optional).
    ├── requirements.txt         # requirements
    └── README.md

why data folder is empty?
<br><li>since i'm using github free version,it will not allow me to store the big file. 
    <br><li> add the complete data inside data folder before training.
        

How can i train the model?
<br> clone the repository using https://github.com/Ashwath-Shetty/Fraudulent-Transaction-detection.git 
<br>step 1: go to command prompt and navigate to project folder(cd project/folder/path)
<br>step 2: enter pip install - r requirements.txt
<br>step 3 : navigate to src folder (cd path/src)
<br>step 4: type python train.py and hit enter.
<br>after training model will be saved in models folder and train, test data used for training will be stored in data folder.

How to run the app on local host?
<br><li>go to command prompt and navigate to project folder and enter streamlit run app.py
    
## Technical Details
<li> here's the complete EDA notebook
    <br>https://www.kaggle.com/ashwathshetty/fraud-detection-eda/notebook
    <br>if you want to pull just use this command -> kaggle kernels pull ashwathshetty/fraud-detection-eda
<li> here's the Modeling notebook
    <br>https://www.kaggle.com/ashwathshetty/plentina-code-challenge/notebook
<li> some high level details about the modelling
    <br> 5 fold stratified cross validation has been used to evaluate the model. stratified is due to the imbalanced data.
    <br> since the data is imbalanced roc-auc score is.
    <br> multiple model has been tried and decision tree worked well at the end.
    <br> randomizedsearchcv with the same 5 folds as above mentioned has been used. (since the data is huge i have avoided the grid searchcv.)
    <br> finally all the models and configurations are exported to joblib format for inference and deployment.
        
## Deployment
<li>Application has been deployed to streamlit cloud and connected github to streamlit for continuous deployment. every commit to the github will automatically deploy to the streamlit.
<br><li>i haven't Dockerized the appication because my PC configuration is very poor but i have added the docker file for future improvements.

## Tools and languages used
1. Python
2. Scikit learn
3. pandas
4. numpy
5. joblib
6. Randomized Serch CV
7. streamlit for development
8. Various ML Modelling and preprocessing techniques.
9. streamlit cloud for deployment
## Future improvement
<br><li>improve the UI for APP and cover more edge cases and error handling.
<br><li>improved hyper parameter optimization using gridsearchcv
<br><li>Stacking and Ensembling.
