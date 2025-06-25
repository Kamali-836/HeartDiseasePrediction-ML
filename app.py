# app.py
from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        name = request.form.get('name', 'User')
        
        # Get all 13 required features from the form
        age = int(request.form.get('age'))
        sex = int(request.form.get('sex'))
        cp = int(request.form.get('cp'))
        trestbps = int(request.form.get('trestbps'))
        chol = int(request.form.get('chol'))
        fbs = int(request.form.get('fbs'))
        restecg = int(request.form.get('restecg'))
        thalach = int(request.form.get('thalach'))
        exang = int(request.form.get('exang'))
        oldpeak = float(request.form.get('oldpeak'))
        slope = int(request.form.get('slope'))
        ca = int(request.form.get('ca'))
        thal = int(request.form.get('thal'))
        
        # Create input array for prediction
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Format output
        if prediction[0] == 0:
            result = f"Hi {name}, you are likely not at risk of heart disease."
            advice = "Keep it up!"
            status = "healthy"
        else:
            result = f"Hi {name}, you might be at risk of heart disease."
            advice = "Please consult a doctor."
            status = "at-risk"
        
        return render_template('index.html', prediction_text=result, advice=advice, status=status)
    
    except Exception as e:
        return render_template('index.html', 
                             prediction_text=f"An error occurred: {str(e)}",
                             advice="Please ensure all form fields are filled correctly.",
                             status="error")

if __name__ == '__main__':
    app.run(debug=True)
