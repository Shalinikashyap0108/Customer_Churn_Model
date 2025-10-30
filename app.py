from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

import os
import pickle

# Get absolute path to model.pkl regardless of where the script is run
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load both model and scaler
with open(MODEL_PATH, "rb") as f:
    model, scaler = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)[0]
    result = "Customer is likely to churn." if prediction == 1 else "Customer will stay."
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
