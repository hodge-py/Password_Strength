from flask import Flask, render_template
from flask import request
import pandas as pd
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    projectpath = request.form['projectFilepath']
    print(projectpath)
    lens = len(projectpath)
    upper = any(char.isupper() for char in projectpath)
    lower = any(char.islower() for char in projectpath)
    special = any(char in special_characters for char in projectpath)
    number = any(char.isnumeric() for char in projectpath)
    tmpdf = pd.DataFrame(data={'password_length': [lens], 'Upper': [upper], 'Lower': [lower], 'Special': [special], 'Number': [number]})
    print(tmpdf)
    return render_template('output.html',password=projectpath)