# Fraudulent-Transaction-Detection
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
because i'm using github free version and it can't store the big file. add the complete data inside data folder.

How can i train the model?
step 1: go to command prompt
step 2: enter pip install - r requirements.txt
step 3 : navigate to src folder (cd path/src)
step 4: type python train.py and hit enter.
after training model will be saved in models folder and train, test data used for training will be stored in data folder.

How to run the app on local host?
go to command prompt and enter streamlit run app.py

## Deployment
Application has been deployed to streamlit cloud and connected github to streamlit for continuous deployment. every commit to github will automatically deploy to the streamlit.
i haven't Dockerized the appication because my PC configuration is very poor but i have added the docker file for future improvements.

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
improve the UI for APP and cover more edge cases and error handling.
improved hyper parameter optimization using gridsearchcv
Stacking and Ensembling.
