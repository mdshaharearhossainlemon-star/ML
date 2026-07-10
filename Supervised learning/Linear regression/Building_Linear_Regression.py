import numpy as np

class LinearRegression():

    def __init__(self, learning_rate, no_of_iterations ):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations

    def fit(self, X, Y):
        #number of training examples and number of features
        self.m, self.n = X.shape
        #initiating the weight and bias
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        #implementing Gradient Decent
        for i in range(self.no_of_iterations):
            self.update_weight()

    def  update_weight(self):
        Y_prediction = self.predict(self.X)

        # calculate gradients  
        dw = -(2 * (self.X.T).dot(self.Y - Y_prediction)) / self.m
        db = -2 * np.sum(self.Y - Y_prediction) / self.m
        #updating the weights
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db



    def predict(self, X):
         return X.dot( self.w ) + self.b
         

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'A:\CodeMania\7TH MODULE\salary_data.csv')
print(df.head())
print(df.tail())
#Splitting the feature & target
X = df.iloc[:, :-1].values
Y = df.iloc[:, 1].values
print(X)
print(Y)
#train

X_train, X_test, Y_train, Y_test =train_test_split(X, Y, test_size=0.33, random_state=2)
model = LinearRegression(learning_rate=0.02, no_of_iterations=1000)
model.fit(X_train, Y_train)
test_data_prediction = model.predict(X_test)
print(test_data_prediction)

#graph plot
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_test, test_data_prediction, color='blue')
plt.xlabel(' Work Experience')
plt.ylabel('Salary')
plt.title(' Salary vs Experience')
plt.show()