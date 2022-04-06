# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 15:24:33 2022

@author: YASHIM GABRIEL
"""

import numpy as np 
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('GradientBoost1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    te_me = float(request.form['te_me'])
    ar_me = float(request.form['ar_me'])
    sm_me = float(request.form['sm_me'])
    co_me = float(request.form['co_me'])
    con_me = float(request.form['con_me'])
    sy_me = float(request.form['sy_me'])
    fdm = float(request.form['fdm'])
    ra_se = float(request.form['ra_se'])
    te_se = float(request.form['te_se'])
    ar_se = float(request.form['ar_se'])
    sm_se = float(request.form['sm_se'])
    co_se = float(request.form['co_se'])
    con_se = float(request.form['con_se"'])
    cps = float(request.form['cps'])
    sy_se = float(request.form['sy_se'])
    fds = float(request.form['fds'])
    sm_wo = float(request.form['sm_wo'])
    co_wo = float(request.form['co_wo'])
    con_wo = float(request.form['con_wo'])
    sy_wo = float(request.form['sy_wo'])
    fdw = float(request.form['fdw'])

    final_features = np.array([[te_me,ar_me,sm_me,co_me,con_me,sy_me,fdm,ra_se,te_se,ar_se,sm_se,
                                co_se,con_se,cps,sy_se,fds,sm_wo,co_wo,con_wo,sy_wo,fdw]])
    prediction = model.predict(final_features)
    
    output = prediction[0]
    
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)