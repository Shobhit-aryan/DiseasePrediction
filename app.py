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

@app.route('/symptom.html')
def symp():
    return render_template('symptom.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        symptom1 = request.form['symp1']
        symptom2 = request.form['symp2']
        symptom3 = request.form['symp3']
        symptom4 = request.form['symp4']
        input_symptoms = symptom1+" "+symptom2+" "+symptom3+" "+symptom4
        data = [input_symptoms]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        if(my_prediction==0):
            return render_template('symptom.html', prediction="Paroymsal Positional Vertigo")
        elif (my_prediction == 1):
            return render_template('symptom.html', prediction="AIDS")
        elif (my_prediction == 2):
            return render_template('symptom.html', prediction="Acne")
        elif (my_prediction == 3):
            return render_template('symptom.html', prediction="Alcoholic hepatitis")
        elif (my_prediction == 4):
            return render_template('symptom.html', prediction="Allergy")
        elif (my_prediction == 5):
            return render_template('symptom.html', prediction="Arthritis")
        elif (my_prediction == 6):
            return render_template('symptom.html', prediction="Bronchial Asthma")
        elif (my_prediction == 7):
            return render_template('symptom.html', prediction="Cervical spondylosis")
        elif (my_prediction == 8):
            return render_template('symptom.html', prediction="Chicken pox")
        elif (my_prediction == 9):
            return render_template('symptom.html', prediction="Chronic cholestasis")
        elif (my_prediction == 10):
            return render_template('symptom.html', prediction="Common Cold")
        elif (my_prediction == 11):
            return render_template('symptom.html', prediction="Dengue")
        elif (my_prediction == 12):
            return render_template('symptom.html', prediction="Diabetes")
        elif (my_prediction == 13):
            return render_template('symptom.html', prediction="Dimorphic hemmorhoids(piles)")
        elif (my_prediction == 14):
            return render_template('symptom.html', prediction="Drug Reaction")
        elif (my_prediction == 15):
            return render_template('symptom.html', prediction="Fungal infection")
        elif (my_prediction == 16):
            return render_template('symptom.html', prediction="GERD")
        elif (my_prediction == 17):
            return render_template('symptom.html', prediction="Gastroenteritis")
        elif (my_prediction == 18):
            return render_template('symptom.html', prediction="Heart attack")
        elif (my_prediction == 19):
            return render_template('symptom.html', prediction="Hepatitis B")
        elif (my_prediction == 20):
            return render_template('symptom.html', prediction="Hepatitis C")
        elif (my_prediction == 21):
            return render_template('symptom.html', prediction="Hepatitis D")
        elif (my_prediction == 22):
            return render_template('symptom.html', prediction="Hepatitis E")
        elif (my_prediction == 23):
            return render_template('symptom.html', prediction="Hypertension")
        elif (my_prediction == 24):
            return render_template('symptom.html', prediction="Hyperthyroidism")
        elif (my_prediction == 25):
            return render_template('symptom.html', prediction="Hypoglycemia")
        elif (my_prediction == 26):
            return render_template('symptom.html', prediction="Hypothyroidism")
        elif (my_prediction == 27):
            return render_template('symptom.html', prediction="Impetigo")
        elif (my_prediction == 28):
            return render_template('symptom.html', prediction="Jaundice")
        elif (my_prediction == 29):
            return render_template('symptom.html', prediction="Malaria")
        elif (my_prediction == 30):
            return render_template('symptom.html', prediction="Migraine")
        elif (my_prediction == 31):
            return render_template('symptom.html', prediction="Osteoarthristis")
        elif (my_prediction == 32):
            return render_template('symptom.html', prediction="Paralysis (brain hemorrhage)")
        elif (my_prediction == 33):
            return render_template('symptom.html', prediction=input_symptoms)
        elif (my_prediction == 34):
            return render_template('symptom.html', prediction="Pneumonia")
        elif (my_prediction == 35):
            return render_template('symptom.html', prediction="Psoriasis")
        elif (my_prediction == 36):
            return render_template('symptom.html', prediction="Tuberculosis")
        elif (my_prediction == 37):
            return render_template('symptom.html', prediction="Typhoid")
        elif (my_prediction == 38):
            return render_template('symptom.html', prediction="Urinary tract infection")
        elif (my_prediction == 39):
            return render_template('symptom.html', prediction="Varicose veins")
        elif (my_prediction == 40):
            return render_template('symptom.html', prediction="hepatitis A")
        else:
            return render_template('symptom.html', prediction="Sorry Can't Predict")
    
if __name__=='__main__':
    app.run(debug=True)