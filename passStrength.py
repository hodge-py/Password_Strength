import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
pd.options.display.max_columns = None

df = pd.read_csv('./data/Passwords.csv')

special_characters =  " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

df['password_length'] = df['password'].apply(lambda x: len(x))

df['Upper'] = df['password'].apply(lambda x: any(char.isupper() for char in x))

df['Lower'] = df['password'].apply(lambda x: any(char.islower() for char in x))

df['Special'] = df['password'].apply(lambda x: any(char in special_characters for char in x))

print(df.head(100))

