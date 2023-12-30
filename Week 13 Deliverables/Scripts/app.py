# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:23:15 2023

@author: Ashish S
"""

import os
import numpy as np
import pickle as pkl
from flask import Flask
from flask import request 
from flask import render_template

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.getcwd(), 'LR_model.pkl')
model = pkl.load(open(model_path, 'rb'))

lb_enc_path = os.path.join(os.getcwd(), 'lbl_enc.pkl')
lb_enc = pkl.load(open(lb_enc_path, 'rb'))

# Route to the homepage
@app.route('/')
def home():
    
    return render_template('home.html')

# Prediction of inputs from the form
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    features = [x for x in request.form.values()]
    features = [int(val) if val.isdigit() else val for val in features]
    features_upd = [lb_enc.transform([val])[0] if isinstance(val, str) else val for val in features]
    result = model.predict([features_upd])[0]
    result = 'Persistent' if result == 1 else 'Non-Persistent'
    
    return render_template('home.html', prediction_result='Patient is {} to New Therapy Medication'.format(result))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
