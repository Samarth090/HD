import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import accuracy_score

# loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv('HP.csv')

# print first 5 rows of the dataset
heart_data.head()

# print last 5 rows of the dataset
heart_data.tail()

# number of rows and columns in the dataset
heart_data.shape

# getting some info about the data
heart_data.info()

# checking for missing values
heart_data.isnull().sum()

# statistical measures about the data
heart_data.describe()

# checking the distribution of Target Variable
heart_data['Heart Disease'].value_counts()

#1 --> Defective Heart

#0 --> Healthy Heart

#Splitting the Features and Target

X = heart_data.drop(columns='Heart Disease', axis=1)
Y = heart_data['Heart Disease']

print(X)

print(Y)

#Splitting the Data into Training data & Test Data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

#Model Training

#Logistic Regression

model = LogisticRegression()

# training the LogisticRegression model with Training data
model.fit(X_train, Y_train)


#Make pickle file of our model

pickle.dump(model,open("model.pkl","wb"))

