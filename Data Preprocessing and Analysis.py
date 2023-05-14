import numpy as np
import pandas as pd

data = pd.read_csv('datasets/loan_prediction_dataset.csv')


#Filling the null values of numerical field with mean value
data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mean())
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mean())

#Filling the null values of categorical field with mode
data['Gender'] = data["Gender"].fillna(data['Gender'].mode()[0])
data['Married'] = data["Married"].fillna(data['Married'].mode()[0])
data['Dependents'] = data["Dependents"].fillna(data['Dependents'].mode()[0])
data['Self_Employed'] = data["Self_Employed"].fillna(data['Self_Employed'].mode()[0])
data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])


#Log Transformation
data['ApplicantIncomeLog'] = np.log(data['ApplicantIncome']+1)
data['CoapplicantIncomeLog'] = np.log(data['CoapplicantIncome']+1)
data['LoanAmountLog'] = np.log(data['LoanAmount']+1)
data['Loan_Amount_Term_Log'] = np.log(data['Loan_Amount_Term']+1)

#Calculating Total Income from ApplicantIncome and CoapplicantIncome
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data['TotalIncomeLog'] = np.log(data['TotalIncome'])



#Dropping the redundant columns
cols = ['ApplicantIncome', 'CoapplicantIncome', "LoanAmount", "Loan_Amount_Term", "TotalIncome", 'Loan_ID', 'CoapplicantIncomeLog']
data = data.drop(columns=cols, axis=1)


#Numerical Encoding of Categorical Variables
data['Gender'].replace(to_replace=['Male','Female'], value=[1,0], inplace=True)
data['Married'].replace(to_replace=['Yes','No'], value=[1,0],inplace=True)
data['Education'].replace(to_replace=['Graduate','Not Graduate'], value=[1,0], inplace=True)
data['Self_Employed'].replace(to_replace=['Yes','No'], value=[1,0],inplace=True)
data['Property_Area'].replace(to_replace=['Urban','Semiurban','Rural'], value=[2,1,0],inplace=True)
data['Loan_Status'].replace(to_replace=['Y','N'], value=[1,0],inplace=True)
data['Dependents'].replace(to_replace=['3+'], value=[3],inplace=True)


# #Function for Standarizing data
# def standarize(arr):
#     average = np.mean(arr)
#     std_dev = np.std(arr)

#     output = []

#     for i in range(len(arr)):
#         output.append( (arr[i]-average)/std_dev )
#     return np.array(output)

# #Data Standarization
# data['ApplicantIncomeLog'] = standarize(data['ApplicantIncomeLog'])
# data['LoanAmountLog'] = standarize(data['LoanAmountLog'])
# data['Loan_Amount_Term_Log'] = standarize(data['Loan_Amount_Term_Log'])
# data['TotalIncomeLog'] = standarize(data['TotalIncomeLog'])



#Randomize the dataset
data = data.sample(
    frac=1,random_state=99999
)


#Splitting the data to train and test data with 80% train data and 20% test data
n_train = int(len(data)*0.75)
n_test = int(len(data)*0.25)

train_data = data[0:n_train]
test_data = data[n_train:n_train+n_test]

print(f'''
train_data = {len(train_data)} 
test_data = {len(test_data)}
''')


#Saving the train and test data to separate files
train_data.to_csv('datasets/train_data.csv', index=0)
test_data.to_csv('datasets/test_data.csv',index=0)