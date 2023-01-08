#!/usr/bin/env python
# coding: utf-8

# ### 1. Importing the essential modules

# In[1]:


import numpy as np #Numpy is used for data manipulation


# ### 2. Mathematics for Logistic Regression

# The Sigmoid Function
# 
# $$ s(x) = \frac{1}{1 + e^{-x}} $$

# 
# The log loss function
# $$ -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)] $$
# 
# 

# Gradient of log loss
# $$ \frac{\partial}{\partial w_j} (-\frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]) = \frac{1}{N} \sum_{i=1}^{N} (p_i - y_i) x_{ij} $$

# 
# 
# $$ \frac{\partial}{\partial b} (-\frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]) = \frac{1}{N} \sum_{i=1}^{N} (p_i - y_i) $$

# ### 3. Implementation of LogisticRegression Algorithm via OOP Method

# #### 3.1 The implementation of sigmoid function for logistic regression

# In[2]:


#The sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# #### 3.2 Sigmoid Function Description

# In[6]:


# #Uncommeting this block of code will show the graph of the sigmoid function and its values

# import matplotlib.pyplot as plt  #matplotlib is used for visualization

# fig = plt.figure()
# axes1 = fig.add_axes([0, 0, 1, 1])

# inputs = np.array(range(-10, 10))
# outputs = sigmoid(inputs)

# axes1.plot(inputs, outputs, label = "Sigmoid Graph",color = '#133F5C')
# axes1.axhline(0, color = "black", ls = "--", lw = 0.5, alpha = 0.5)
# axes1.axvline(0, color = "black", ls = "--", lw = 0.5, alpha = 0.5)
# axes1.axhline(y = 0.5, xmin=0.5, xmax=0.55, color = "red", ls = "--", lw = 0.7, alpha = 1, label = 'y=0.5 for x=0' )
# axes1.set_title('Sigmoid Graph')
# axes1.set_xlabel('X-axis')
# axes1.set_ylabel('Y-axis')

# plt.legend()


# #### 3.3 The Implementation of Logistic Regression Class

# In[108]:


#Implementing the Logistic regression class

class LogisticRegression:

    #The constructor with learning rate and number of iterations
    #Default learning rate = 0.1 and number of iterations = 10,000
    
    def __init__(self, lr=0.1, n_iters = 10_000):
        self.lr = lr
        self.n_iters = n_iters


    #The main fit method, that accepts the x_train and y_train values to adjust weights and biases
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.n_iters):

            linear_predictions = np.dot(X, self.weights) + self.bias
            predictions = sigmoid(linear_predictions)

            
            
            #Using the standard gradient descent algorithm to adjust the weights and biases
            #The gradient of the log loss function is shown in section 2.Mathematics
            dw = (1/n_samples) * np.dot(X.T, predictions-y)
            db = (1/n_samples) * np.sum(predictions-y)
            
            #adjusting the weights and biases for n_iters times
            self.weights = self.weights - self.lr*dw
            self.bias = self.bias-self.lr*db



            
    
    #After adjusting the weights and biases, the predict method accepts the testing data in form of numpy arrays and
    # outputs the class_pred variable that holds the predicted output
    def predict(self,X):
        linear_predictions = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_predictions)

        
        #if the sigmoid function returns value >= 0.5 then we classify as 1
        #else we classify as 0 by list comprehension
        class_pred=[1 if y>=0.5 else 0 for y in y_pred]

        return np.array(class_pred)

        #function written above returns all data
        #make new function that returns only data which is submitted
    def predict_for_one(self,X):
        linear_predictions = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_predictions)
        class_pred = [1 if y_pred >= 0.5 else 0]
        return class_pred



# ### 4. The Implementation of Loss Class

# #### 4.1 The loss class is class that holds all the methods and attributes for displaying the losses and accuracy of the model
# 

# In[107]:


class Loss():
    def conf_mat(self,class_pred, y_true):
        tp=0
        fp=0
        tn=0
        fn=0
        for items in zip(class_pred, y_true):
            if items==(1,1):
                tp+=1
            elif items==(1,0):
                fp+=1
            elif items==(0,1):
                fn+=1
            else:
                tn+=1
                
                
        print(f'{tp=}')
        print(f'{fp=}')
        print(f'{fn=}')
        print(f'{tn=}')
                
        confusion_matrix=np.array([tp,fp,fn,tn]).reshape(2,2)
        return confusion_matrix

    
    def accuracy(self, class_pred, y_true):
        return np.sum(class_pred==y_true)/len(y_true)


# In[ ]:




