'''
Code to evaluate all models using the following eval metrics
R2 - coefficient of determination
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
'''

import pandas as pd
import warnings
import pickle
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sqlalchemy import create_engine
from platform import python_version
from modeling import predict
from modeling import linear_regressor
from modeling import gradient_boost_regressor
from modeling import nn_regressor
from modeling import random_forest_regressor
from modeling import svm_regressor
from modeling import ransac_regressor
from modeling import gaussian_process_regressor

warnings.filterwarnings("ignore")

#----------------------------------------------
prediction_year = 2024 #year or None
#----------------------------------------------
root = 'NCAAM_Web_App\\Python\\'
csv_path = root + r'CSV_Data\\'
beginning_year = 2010
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023]
if prediction_year is not None and prediction_year in years: years.remove(prediction_year)
if beginning_year in years: years.remove(beginning_year)
df = pd.read_csv(csv_path+f'{beginning_year}\\{beginning_year}_data.csv')
df = df.iloc[:,2:]

for year in years:
    small_df = pd.read_csv(csv_path+f'{year}\\{year}_data.csv')
    small_df = small_df.iloc[:,2:]
    df = pd.concat([df,small_df])

X = df.drop('Score_Dif',axis= 1) 
y = df['Score_Dif'] 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.25, random_state=40) 


with open(root + f'modeling\\best-model{python_version()}.pkl', 'rb') as f:
    model = pickle.load(f)
r_squared = model.score(X, y)
#mse = mean_squared_error(y_test, model)
#mae = mean_absolute_error(y_test, model)

if prediction_year is not None:
    prediction = predict.predict(str(prediction_year),model,root)
    print(prediction)
    df = pd.DataFrame(prediction, columns=["Id", "Year", "Game", "GameNum", "Result"])
    df.to_csv(f'{root}evaluation/{prediction_year}_tournament_results.csv', index=False)
    engine = create_engine('mssql+pyodbc://(LocalDb)\MSSQLLocalDB/NCAAM_Stats?&driver=ODBC+Driver+17+for+SQL+Server', use_setinputsizes=False)
    df.to_sql("Tournament", engine, if_exists="replace", index=False)