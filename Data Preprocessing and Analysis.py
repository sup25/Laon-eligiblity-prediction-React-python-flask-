#!/usr/bin/env python
# coding: utf-8

# ### 1. Importing the necessary modules

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


plt.style.use('ggplot')


# ### 2. Loading the dataset

# In[3]:


data = pd.read_csv(r'loan_prediction_dataset.csv')


# ### 3. Exploratory Data Analysis and Cleaning

# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


#finding the null values
data.isnull().sum()


# In[8]:


#filling the null values of numerical features with mean values
data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mean())
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mean())


# In[9]:


#filling the null values of categorical features with mode
data['Gender'] = data["Gender"].fillna(data['Gender'].mode()[0])
data['Married'] = data["Married"].fillna(data['Married'].mode()[0])
data['Dependents'] = data["Dependents"].fillna(data['Dependents'].mode()[0])
data['Self_Employed'] = data["Self_Employed"].fillna(data['Self_Employed'].mode()[0])
data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])


# In[10]:


data.isnull().sum()


# #### 3.1 Categorical Attributes Visualization

# In[11]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax1.bar(x = data['Gender'].unique(),height = data['Gender'].value_counts(),color = ['#133F5C','#EB5F5E'])
ax1.set_title('Customers Count by Gender')


ax2 = fig.add_axes([1.1,0,1,1])
ax2.bar(x = data['Married'].unique(),height = data['Married'].value_counts(), color = ['#133F5C','#EB5F5E'])
ax2.set_title('Customers Count by Marriage')


ax3 = fig.add_axes([2.2,0,1,1])
ax3.bar(x = data['Dependents'].unique(), height = data['Dependents'].value_counts(),color = ['#133F5C','#EB5F5E','#58508D', '#BC5090'])
ax3.set_title('Customers Count by Dependents')


ax4 = fig.add_axes([0,-1.2,1,1])
ax4.bar(x = data['Education'].unique(), height = data['Education'].value_counts(),color = ['#133F5C','#EB5F5E'])
ax4.set_title('Customer count by Education')

ax5 = fig.add_axes([1.1,-1.2,1,1])
ax5.bar(x = data['Self_Employed'].unique(), height = data['Self_Employed'].value_counts(), color = ['#133F5C','#EB5F5E'] )
ax5.set_title('Customer count by Employement')


ax6 = fig.add_axes([2.2,-1.2,1,1])
ax6.bar(x = data['Property_Area'].unique(), height = data['Property_Area'].value_counts(), color = ['#133F5C','#EB5F5E','#BC5090'] )
ax6.set_title('Customer count by Property Area')



plt.show()


# In[ ]:





# ### 4. Log Transformation of Numerical Features

# In[12]:


data['ApplicantIncomeLog'] = np.log(data['ApplicantIncome']+1)
data['CoapplicantIncomeLog'] = np.log(data['CoapplicantIncome']+1)
data['LoanAmountLog'] = np.log(data['LoanAmount']+1)
data['Loan_Amount_Term_Log'] = np.log(data['Loan_Amount_Term']+1)

#Calculating Total Income
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data['TotalIncomeLog'] = np.log(data['TotalIncome'])


# In[13]:


data.head()


# In[14]:


#Dropping Unnecessary Columns

cols = ['ApplicantIncome', 'CoapplicantIncome', "LoanAmount", "Loan_Amount_Term", "TotalIncome", 'Loan_ID', 'CoapplicantIncomeLog']
data = data.drop(columns=cols, axis=1)
data.head()


# ### 5. Numerical Encoding of Categorical Features

# In[15]:


#cols = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']

data['Gender'].replace(to_replace=['Male','Female'], value=[1,0], inplace=True)
data['Married'].replace(to_replace=['Yes','No'], value=[1,0],inplace=True)
data['Education'].replace(to_replace=['Graduate','Not Graduate'], value=[1,0], inplace=True)
data['Self_Employed'].replace(to_replace=['Yes','No'], value=[1,0],inplace=True)
data['Property_Area'].replace(to_replace=['Urban','Semiurban','Rural'], value=[2,1,0],inplace=True)
data['Loan_Status'].replace(to_replace=['Y','N'], value=[1,0],inplace=True)
data['Dependents'].replace(to_replace=['3+'], value=[3],inplace=True)


# In[16]:


data.head(5)


# ### 6. Data Standarization

# In[17]:


def standarize(arr):
    
    average = np.mean(arr)
    std_dev = np.std(arr)
    
    output = []
    
    for i in range(len(arr)):
        output.append( (arr[i]-average)/std_dev )
    
    return np.array(output)
    


# In[18]:


data['ApplicantIncomeLog'] = standarize(data['ApplicantIncomeLog'])
data['LoanAmountLog'] = standarize(data['LoanAmountLog'])
data['Loan_Amount_Term_Log'] = standarize(data['Loan_Amount_Term_Log'])
data['TotalIncomeLog'] = standarize(data['TotalIncomeLog'])


# In[19]:


data.head()


# ### 7. Splitting the Train and Test Data

# In[20]:


#shuffling the dataset
data = data.sample(
    frac=1,random_state=99
)


# In[21]:


n_train = int(len(data)*0.75)
n_test = int(len(data)*0.25)

train_data = data[0:n_train]
test_data = data[n_train:n_train+n_test]

print(len(train_data), len(test_data))


# In[22]:


train_data.to_csv('train_data.csv', index=0)
test_data.to_csv('test_data.csv',index=0)


# In[ ]:




