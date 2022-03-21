# Fraudulent-Transaction-Detection
## Live Demo
<br><li> to test with UI(currently not updated from the old version, so it might have some issues) 
--> https://share.streamlit.io/ashwath-shetty/fraudulent-transaction-detection/main/app.py
<br><li> Fast API(detailed instruction about how to test is in 'Testing the Deployed FastAPI'Section below )
--> https://fraud-t-detection.herokuapp.com/docs

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
    ├── app.py                   # deployed main app code for streamlit
    ├── Procfile                 # Procfile to deploy to Heroku
    ├── requirements.txt         # requirements
    ├── fast_api.py              # main FastApi file.
    ├── api_test.py              #FastApi testing file.
    ├── Dockerfile               # to Dockerize
    └── README.md

<b>why data folder is empty?</b>
<br><li>since i'm using github free version,it will not allow me to store the big files. 
    <br><li> add the complete data inside data folder before training.

<b>How can i train the model?</b>
<br>step 1: clone the repository using https://github.com/Ashwath-Shetty/Fraudulent-Transaction-detection.git 
<br>step 2: add the data inside data folder and change the training file path to your path in the config file(which is inside src folder).
<br>step 3: go to command prompt and navigate to the project folder(cd project/folder/path)
<br>step 4: enter pip install - r requirements.txt
<br>step 5 : navigate to src folder (cd path/src)
<br>step 6: type python train.py and hit enter.
<br>after training model will be saved in models folder and train, test data used for training will be stored in the data folder.

<b>How to run the app on local host?</b>
<br> if you just want to check the deployed api, you can skip this and check the next section
<br><li>to test streamlit UI based application -> go to command prompt and navigate to project folder and enter streamlit run app.py
<br><li> go to command prompt and navigate to project folder and enter uvicorn fast_api:app --reload
  <br> go to browser and visit http://127.0.0.1:8000/docs

## Testing the Deployed FastAPI
<br> <li>all you need is api_test.py file and python installed in the system. 
<br> <li>just run the file using python api_test.py and you will get the response printed on the console.
<br><li> url to test if you have your own testing code https://fraud-t-detection.herokuapp.com/is-fraud (you can check the json format in api_test.py)
<br> if you want to change the data go to line 11 inside api_test.py where you can see json={} and change the data you want to.

    
## Technical Details
<li>here's the complete EDA notebook
<br>https://www.kaggle.com/ashwathshetty/fraud-detection-eda/notebook
 <br>if you want to pull just use this command -> kaggle kernels pull ashwathshetty/fraud-detection-eda
<li> here's the Modeling notebook
    <br>https://www.kaggle.com/ashwathshetty/plentina-code-challenge/notebook
<li> some high level details about the modelling
    <br>1. 5 fold stratified cross validation has been used to evaluate the model. stratified is due to the imbalanced data.
    <br>2. since the data is imbalanced roc-auc score is used as a evaluation metrics. train has an average score of 0.97184328592481 and test 0.9431405985587756
    <br>3. multiple model has been tried and decision tree worked well at the end.
    <br>4. randomizedsearchcv with the same 5 folds as above mentioned has been used. (since the data is huge i have avoided the grid searchcv.)
    <br>5. finally all the models and configurations are exported to joblib format for inference and deployment.
        
## Deployment
<b>Streamlit Deployment</b>
<li>Application has been deployed to streamlit cloud and connected github to streamlit for continuous deployment. every commit to the github will automatically deploy to the streamlit.
<br><b>Fast API and Heroku Deployment</b>
<br><li>Fast API has been used to develop the API and it has been deployed to Heroku cloud platform.every commit to the github will automatically deploy to the Heroku for continuous deployment.
<br><li>i haven't Dockerized the appication because my PC configuration is very poor but i have added the docker file for future improvements.
<br><li> and also there's a Dockerrun.aws.json file which will help to deploy the dockerized container to AWS Fargate.

## Tools and languages used
1. Python
2. Scikit learn
3. pandas
4. numpy
5. joblib
6. Randomized Search CV
7. streamlit for development
8. Various ML Modelling and preprocessing techniques.
9. streamlit cloud for deployment
10. Fast API for API Development.
11. Heroku for Fast API deployment.
12. uvicorn and gunicorn.
## Future improvement
<br><li>improve the UI for APP and cover more edge cases and error handling.
<br><li>improved hyper parameter optimization using gridsearchcv
<br><li>Stacking and Ensembling.
<br><li>Packaging using Docker.

## Reach out to me here
check out my [portfolio](https://ashwathshetty.netlify.app/)
