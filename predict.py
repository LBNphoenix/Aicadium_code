import pandas as pd 
import os 
import numpy as np
import pickle
import joblib
import sklearn
import sys

from processing import feature_bin

from sklearn.ensemble import RandomForestClassifier

PATH = sys.argv[1]
print('Predicting',PATH)
df = pd.read_csv(PATH)
df.drop_duplicates()
df_x = df.drop('Revenue', axis = 1)
df_y = df['Revenue']

predict_model = joblib.load("predict_model.joblib")

df_x_ip = feature_bin(df_x).values
df_y_ip = df_y = df['Revenue'].astype('category').cat.codes.astype('int64').values
y_pred = predict_model.predict(df_x_ip)
df_predict = pd.DataFrame({'Revenue':np.array(y_pred, dtype=bool)})
df_predict.to_csv('predict.csv')
print('predict.csv created')
