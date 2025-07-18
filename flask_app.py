import numpy as np
from flask import Flask, render_template
from flask import request
import pandas as pd
import pickle
import os

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/output', methods=['POST'])
def output():
    with open(f'{dir_path}/data/rockyou-75.txt', 'r') as f:
        common_passwords = [line.strip().lower() for line in f if line.strip()]

    def check_common_substrings(password):
        password = str(password)
        password = password.lower()

        for i in range(len(password)):
            for j in range(i + 3, len(password)):  # substrings of length >= min_length
                if password[i:j] in common_passwords:
                    return True
        return False
    special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    projectpath = request.form['projectFilepath']
    lens = len(projectpath)
    upper = any(char.isupper() for char in projectpath)
    lower = any(char.islower() for char in projectpath)
    special = any(char in special_characters for char in projectpath)
    number = any(char.isnumeric() for char in projectpath)
    dftmp = pd.DataFrame(data={"password_length": [lens],"upper": [upper],"lower": [lower],"special": [special],"number": [number],"has_common_word": [check_common_substrings(projectpath)]})
    loaded_model = pickle.load(open(f'{dir_path}/final_model.sav', 'rb'))
    prediction = loaded_model.predict(dftmp)
    if prediction == 0:
        prediction = 'Very Weak'
    elif prediction == 1:
        prediction = 'Weak'
    elif prediction == 2:
        prediction = 'Medium'
    elif prediction == 3:
        prediction = 'Strong'
    else:
        prediction = 'Very Strong'
    return render_template('output.html',password=prediction, passName=projectpath)