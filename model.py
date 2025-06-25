# model.py
# importing dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# data collection and processing
# loading csv file to pandas df
hdf = pd.read_csv('heart.csv')

# print first five records
print(hdf.head())

# separate features and target
X = hdf.drop(columns='target', axis=1)
Y = hdf['target']

# split data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# evaluate model
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data:', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data:', test_data_accuracy)

# save the trained model
pickle.dump(model, open('model.pkl', 'wb'))
print('Model saved successfully')
