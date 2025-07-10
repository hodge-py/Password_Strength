import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

pd.options.display.max_columns = None

df = pd.read_csv('./data/Passwords.csv')

special_characters =  " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

print(df.head(10))

df['password_length'] = df['password'].apply(lambda x: len(x))

df['Upper'] = df['password'].apply(lambda x: any(char.isupper() for char in x))

df['Lower'] = df['password'].apply(lambda x: any(char.islower() for char in x))

df['Special'] = df['password'].apply(lambda x: any(char in special_characters for char in x))

X = df[['password_length','Upper','Lower','Special']]

y = df['strength']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)

preds = clf.predict(X_test)

print(classification_report(y_test, preds))





