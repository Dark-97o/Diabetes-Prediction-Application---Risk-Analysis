# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest Classifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Form se data uthana
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        # Data ko array mein convert karna
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        
        # Prediction karna
        my_prediction = classifier.predict(data)
        
        # Probability nikalna (Diabetic hone ka chance)
        prob = classifier.predict_proba(data)
        probability_score = round(prob[0][1] * 100, 2)
        
        # Result page par SAARE values bhej rahe hain (graph ke liye)
        return render_template('result.html', 
                               prediction=int(my_prediction[0]),
                               probability=probability_score,
                               pregnancies=preg,
                               glucose=glucose,
                               bp=bp,
                               skin_thickness=st,
                               insulin=insulin,
                               bmi=bmi,
                               dpf=dpf,
                               age=age)

if __name__ == '__main__':
    app.run(debug=True)