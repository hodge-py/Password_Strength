import numpy as np
from flask import Flask, render_template
from flask import request
import pandas as pd
import pickle
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    with open('./data/rockyou-75.txt', 'r') as f:
        common_passwords = [line.strip().lower() for line in f if line.strip()]
    def check_common_substrings(password):
        password = password.lower()
        return any(pw for pw in common_passwords if pw in password)
    special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    projectpath = request.form['projectFilepath']
    lens = len(projectpath)
    upper = any(char.isupper() for char in projectpath)
    lower = any(char.islower() for char in projectpath)
    special = any(char in special_characters for char in projectpath)
    number = any(char.isnumeric() for char in projectpath)
    newArr = [[check_common_substrings(projectpath), lens, upper, lower, special, number]]
    loaded_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = loaded_model.predict(newArr)
    if prediction == 0:
        prediction = 'Weak'
    elif prediction == 1:
        prediction = 'Medium'
    else:
        prediction = 'Strong'
    return render_template('output.html',password=prediction, passName=projectpath)