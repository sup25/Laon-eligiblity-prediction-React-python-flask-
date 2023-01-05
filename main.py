#!/usr/bin/env python
# coding: utf-8

# ## The main file is used for abstract use of the model

# In[12]:


import numpy as np
import pandas as pd
from LogisticRegression import LogisticRegression
from LogisticRegression import Loss


# In[13]:


train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')


# In[14]:


xtrain, ytrain = train_data.drop(columns = 'Loan_Status', axis = 1), train_data['Loan_Status']
xtest, ytest = test_data.drop(columns = 'Loan_Status', axis =1), test_data['Loan_Status']

xtrain = np.array(xtrain)
ytrain = np.array(ytrain)

xtest= np.array(xtest)
ytest =  np.array(ytest)


# In[15]:


clf = LogisticRegression(lr =0.01, n_iters=10000)


# In[16]:


clf.fit(xtrain, ytrain)
y_pred = clf.predict(xtest)
l = Loss()
print(l.conf_mat(y_pred, ytest))
print('\n')
print('Accuracy = ',l.accuracy(y_pred, ytest))


# In[ ]:

#code below are done to fetch data from React Component
from flask import Flask,request
import math
import json


app= Flask(__name__)
#Members api routes

@app.route("/members")
def members():
    return {}



@app.route('/api/send-data', methods=['POST'])
def send_data():
  data = request.json['data']
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
  applicationIncomelog=math.log(int(data['applicantIncome']))
  loanamountlog=math.log(int(data['loanAmount']))
  loanamounttermlog=math.log(int(data['loanAmountTerm']))
  totalincomelog=math.log(int(data['totalIncome']))


  # Process the data and return a response
  data_list = [gender,married,dependent,education,selfemployed,creditHistory, propertyArea,applicationIncomelog,loanamountlog, loanamounttermlog,totalincomelog
] 
#   data_numpy=np.array(data_list)
#   data_numpy=np.reshape (1,11)
#   y_pred = clf.predict(data_list)
  print(data_list)
  return { 'message': "done" }



   

if __name__=="__main__":
    app.run(debug=True)



