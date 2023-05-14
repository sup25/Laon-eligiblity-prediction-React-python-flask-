
#Importing the necessery Modules
#Numpy is used for Matrix Manipulation
import numpy as np 

#Implementation of Logistic Regression Class
#All the input parameters of the methods in LogisticRegression Class should be in the form of numpy arrays
class Logistic_Regression:
    #The constructor of LogisticRegression class initializes the learning rate and number of iterations with 
    #default arguements lr=0.01 and n_iters=10000
    def __init__(self, lr=0.01, n_iters=10_000):
        self.lr = lr
        self.n_iters = n_iters

        
    #Implementation of sigmoid Activation Function
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))

    
    #The fit method accepts the training data and actual classes as X and y respectively.
    #The data type of X and y should also be numpy.ndarray
    def fit(self,X,y):
        #n_samples = number of training data points
        #n_features = number of features the training data has
        n_samples, n_features = X.shape

        #initializing the weights with small random values
        self.weights = np.random.randn(n_features) * 0.1

        #initializing the bias with 0
        self.bias = 0
        
        for i in range(self.n_iters):
            #using the y = wx + b equation to predict the linear predictions of the training data
            linear_predictions = np.dot(X, self.weights) + self.bias
            
            #passing the linear_predictions to the sigmoid activation function to calculate probabilites
            sigmoid_predictions = self.sigmoid(linear_predictions)

            #Calculating and minimizing the loss with standard gradient descent algorithm
                #The loss function that we will use is log-loss/Binary Cross-Entropy
                #given by the equation
                # -(sum(y*log(yhat) +  (1-y)*(log(1-yhat))))/N

                #The gradient of log loss function is given by the equations
                #dw = sum(x*(yhat - y))/N
                #db = sum(yhat - y)/N

            if not i % np.ceil(0.1*self.n_iters):
                
                loss = self.__Loss(y, sigmoid_predictions)
                class_pred = self.__converter(sigmoid_predictions)
                acc = self.Accuracy(y,class_pred)

                #Display the Losses and accuracy for every 10% of of the number of total iterations               
                print('----------------------------------------------------------------------------------')
                print(f'Fitting...Iteration {i}....Loss:{loss}.....Accuracy:{acc}')
                print('----------------------------------------------------------------------------------')


            #Calculating the gradient
            dw = (1/n_samples) * np.dot(X.T, sigmoid_predictions-y)
            db = (1/n_samples) * np.sum(sigmoid_predictions-y)


            #adjusting the weights and biases
            self.weights = self.weights - self.lr*dw
            self.bias = self.bias - self.lr*db
            
        return self.weights, self.bias

    #After adjusting the weights and biases, the predict method accepts the input (X) in the form of
    #numpy.ndarray and outputs the class_pred variable that holds the predicted output

    def predict(self,X):

        linear_predictions = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(linear_predictions)

        #If the sigmoid function returns values >=0.5 then we classify it as 1
        #else we classify it as 0 

        class_pred = self.__converter(y_pred)
        return class_pred



    def predict_for_one(self,X):
        linear_predictions = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(linear_predictions)
        class_pred = [1 if y_pred >= 0.5 else 0]
        return class_pred
    
    
    
    #The converter method turns probabilities into classes
    def __converter(self, y_pred):
        class_pred = [1 if y>=0.5 else 0 for y in y_pred]
        return np.array(class_pred)
    

    
    #Calculate the log loss for given probabilities and actual classes and return the loss
    def __Loss(self, y_true, y_pred):
        log_loss = 0
        for i in range(len(y_true)):
            y = y_true[i]
            p = y_pred[i]
            log_loss += -(y * np.log(p) + (1 - y) * np.log(1 - p))
        return log_loss/len(y_true)


    #Calculate the accuracy of the model
    def Accuracy(self, y_true, y_pred):
        return np.sum(y_pred==y_true)/len(y_pred)

    
    #Display Confusion Matrix as
    # 
    #     [tp fn]
    #     [fp tn]
    # 
    def ConfusionMatrix(self, y_true, y_pred):
        tp = fp = fn = tn = 0

        for pair in zip(y_true, y_pred):
            if pair == (1,1):
                tp+=1

            elif pair == (1,0):
                fn+=1

            elif pair ==(0,1):
                fp+=1

            else:
                tn+=1
                
        return np.array([tp,fn,fp,tn]).reshape(2,2)