
#Importing the necessary modules
import numpy as np
import pandas as pd
from util.LogisticRegression import Logistic_Regression


#Reading the test and train dataset
train_data = pd.read_csv(r'datasets/train_data.csv')
test_data = pd.read_csv(r'datasets/test_data.csv')

#Splitting the data into features and outputs
xtrain, ytrain = train_data.drop(columns = 'Loan_Status', axis = 1), train_data['Loan_Status']
xtest, ytest = test_data.drop(columns = 'Loan_Status', axis =1), test_data['Loan_Status']

#Converting the csv files into numpy ndarrays for Logistic_Regression module
xtrain = np.array(xtrain)
ytrain = np.array(ytrain)

xtest= np.array(xtest)
ytest =  np.array(ytest)

model = Logistic_Regression(lr = 0.01, n_iters = 50_000)
model.fit(xtrain, ytrain)
class_pred = model.predict(xtest)

#Displaying the accuracy of the model and confusion matrix
# print('\n')
print(model.ConfusionMatrix(ytest, class_pred))
# print('\n')
print(f'Accuracy = {model.Accuracy(ytest, class_pred)}')

# In[ ]:

#code below are done to fetch data from React Component
from flask import Flask,request
import math
import json


app= Flask(__name__)
#Members api routes

# @app.route("/members")
# def members():
#     return {}


@app.route('/api/send-data', methods=['POST'])
def send_data():
  data = request.json['data']

  #data validation
  if int(data['loanAmount']) > 10000000:
    return {"Remarks":'Loan Amount should be in range Rs.10,000 - Rs.1,00,00,000'}


  gender = 0 if data['Gender'] == "Female" else 1
  married = 0 if data['married'] == "No" else 1 
  dependent = int(data['dependents'].split(" ")[0]) 
  education= 0 if data['education'] == "Not Graduate" else 1 
  selfemployed= 0 if data['selfEmployed'] == "No" else 1
  creditHistory = int(data['creditHistory'])
  if data['Area']=='Urban':
    propertyArea=2
  elif data['Area']=='semiUrban':
    propertyArea=1
  else:
    propertyArea=0
  applicationIncomelog=np.log(int(data['applicantIncome']))
  loanamountlog=np.log(int(data['loanAmount']))
  loanamounttermlog=np.log(int(data['loanAmountTerm']))
  totalincomelog= np.log(int(data['totalIncome']))






  # Process the data and return a response
  data_list = [gender,married,dependent,education,selfemployed,creditHistory, propertyArea,applicationIncomelog,loanamountlog, loanamounttermlog,totalincomelog] 
  data_numpy = np.array(data_list)
#   data_numpy=np.reshape (1,11)


  print("-------------Data---------")
  print(data_numpy)
  print("---------------------prediction-------------------")
  y_pred = model.predict_for_one(data_numpy)
  print(y_pred)
  if y_pred[0] == 1:
    y_predictions = "Loan is acceptable!"
  else:
    y_predictions = "Loan is not acceptable"
  print(y_predictions)
  return {"Remarks":y_predictions}
  
if __name__=="__main__":
    app.run(debug=True)