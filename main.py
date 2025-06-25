# main.py
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_and_save_model():
    # Load data
    df = pd.read_csv('heart.csv')
    
    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Evaluate model
    train_accuracy = accuracy_score(y_train, model.predict(X_train))
    test_accuracy = accuracy_score(y_test, model.predict(X_test))
    
    print(f"Training Accuracy: {train_accuracy:.4f}")
    print(f"Testing Accuracy: {test_accuracy:.4f}")
    
    # Save model
    with open('model.pkl', 'wb') as file:
        pickle.dump(model, file)
    
    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_and_save_model()
