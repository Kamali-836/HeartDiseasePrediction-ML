❤️ Heart Disease Prediction using Machine Learning

This project is a web-based application that predicts the risk of heart disease using a trained machine learning model. It takes user input through a simple form and provides health-related feedback based on the prediction.

Features:

1. User-friendly Interface Built with HTML/CSS and Flask - 
The frontend of the application is created using clean HTML and styled with CSS to provide an intuitive and visually appealing user experience.Users can easily navigate the form and input their health parameters without needing any technical knowledge.The Flask framework connects this interface to the backend logic and ML model, ensuring smooth data flow between the UI and prediction system.

2. Uses 13 Medical Parameters as Input - 
The webpage collects 13 essential clinical features that are commonly used in cardiology datasets to assess heart disease risk:

Parameter	Description :

age -	Age of the person  , sex	- Biological sex (0 = Female, 1 = Male) , cp	- Chest pain type (0-3) , trestbps  - Resting blood pressure (mm Hg) , chol - Serum cholesterol (mg/dl) , fbs  - Fasting blood sugar > 120 mg/dl (1 = true; 0 = false) , restecg	- Resting electrocardiographic results (0-2) , thalach -	Maximum heart rate achieved , exang -	Exercise-induced angina (1 = yes; 0 = no) , oldpeak -	ST depression induced by exercise , slope -	Slope of the peak exercise ST segment (0-2) , ca -	Number of major vessels colored by fluoroscopy (0–3) , thal -	Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect). These inputs are validated on the frontend and passed to the ML model for prediction.

3. Predicts Whether the User Is at Risk or Not at Risk of Heart Disease - Once the user submits the form, the collected data is processed and passed to a trained machine learning model.The model evaluates the input based on patterns learned during training and classifies the user into one of two categories: Not at Risk (0) – No significant indicators of heart disease detected. At Risk (1) – Possible indicators of heart disease are present. The result is shown in a popup modal with appropriate messaging.

4. Gives Health Advice Based on the Prediction - After prediction, the user receives personalized health advice: If not at risk, tips focus on maintaining a healthy lifestyle. If at risk, it recommends consulting a doctor and making lifestyle improvements (diet, exercise, stress management).The goal is not only to inform but also to educate and encourage preventive health care.

5. Backend Powered by a Pickled ML Model - A machine learning model (e.g., Logistic Regression) is trained offline using the UCI Heart Disease dataset. After training, the model is serialized using Python’s pickle module and saved as model.pkl. Flask loads this .pkl model when the server starts and uses it for real-time predictions. Benefits of using a pickled model: - Faster predictions, no need to retrain the model on every run, clean separation between training and deployment

Machine Learning Model:

Algorithm Used: Logistic Regression is a supervised classification algorithm used to estimate the probability of a binary outcome (e.g., risk or no risk of heart disease).It works well when the relationship between the dependent variable and the independent variables is linear, which is suitable for medical datasets like this one. Chosen for its simplicity, interpretability, and good performance on small to medium-sized datasets.

Dataset Overview:

Total Records: 1025, Total Features: 14 (13 input features + 1 target), Target column: target (0 = not at risk, 1 = at risk), No missing values found

heart/
│
├── templates/
│   └── index.html        
│
├── model.pkl             
├── app.py                
├── README.md           
├── heart.csv           
├── main.py          
├── HeartDiseasePredictor-ML.pdf          
└── model.py

Disclaimer : This application is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for concerns regarding your heart health or any medical condition. The predictions made by this tool are based on a machine learning model trained on publicly available data and may not reflect real-world accuracy in clinical settings.
