# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:39:01 2020

@author: Asus
"""
from flask import Flask, render_template, request
import pickle

classifier = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        input_symptoms = request.form['input_symptoms']
        data = [input_symptoms]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        if(my_prediction==29):
            return render_template('index.html', prediction="ughh")
        else:
            return render_template('index.html',prediction=my_prediction)
    
if __name__=='__main__':
    app.run(debug=True)