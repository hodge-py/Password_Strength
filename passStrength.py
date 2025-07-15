import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import HistGradientBoostingClassifier
from scipy.sparse import hstack
from scipy.sparse import csr_matrix
import pickle

pd.options.display.max_columns = None

df = pd.read_csv('./data/new_passwords.csv')
print(df.shape)
"""
df = pd.read_csv('./data/Passwords.csv')
df2 = pd.read_csv('./data/pwlds_weak.csv')
df3 = pd.read_csv('./data/pwlds_average.csv')
df4 = pd.read_csv('./data/pwlds_strong.csv')
df2['strength'] = 0
df3['strength'] = 1
df4['strength'] = 2
df = pd.concat([df,df2,df3,df4])
print(df.shape)

with open('./data/rockyou-75.txt', 'r') as f:
    common_passwords = [line.strip().lower() for line in f if line.strip()]

# Function to check for common passwords as substrings
def check_common_substrings(password):
    password = password.lower()
    return any(pw for pw in common_passwords if pw in password)

df['has_common_word'] = df['password'].apply(lambda x: check_common_substrings(x))

df.to_csv('./data/new_passwords.csv', index=False)

"""
special_characters =  " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

df['password_length'] = df['password'].apply(lambda x: len(x))

df['upper'] = df['password'].apply(lambda x: any(char.isupper() for char in x))

df['lower'] = df['password'].apply(lambda x: any(char.islower() for char in x))

df['special'] = df['password'].apply(lambda x: any(char in special_characters for char in x))

df['number'] = df['password'].apply(lambda x: any(char.isnumeric() for char in x))

X = df[['password_length','upper','lower','special','number','has_common_word']]

y = df['strength']

print(y.value_counts())

print(df.head(10))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

clf = GradientBoostingClassifier(learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)

preds = clf.predict(X_test)

print(classification_report(y_test, preds))

filename = 'final_model.sav'
pickle.dump(clf, open(filename, 'wb'))
#tmpdf = pd.DataFrame(data={'password_length': [1], 'upper': [True], 'lower': [False], 'special': [False],'number': [False]})
#print(tmpdf)
#print(clf.predict(tmpdf))





