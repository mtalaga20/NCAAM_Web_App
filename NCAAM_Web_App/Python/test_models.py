'''
Code to evaluate all models using the following eval metrics
R2 - coefficient of determination
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
'''

import pandas as pd
import warnings
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
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

csv_path = r'CSV_Data\\'
beginning_year = 2010
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023]
if prediction_year is not None and prediction_year in years: years.remove(prediction_year)
model_functions = [#linear_regressor.linear_regressor,
                   #ransac_regressor.ransac_regressor,
                   gradient_boost_regressor.gb_regressor,
                   #nn_regressor.nn_regressor, 
                   #random_forest_regressor.random_forest_regressor,
                   #gaussian_process_regressor.gaussian_process_regressor,
                   #svm_regressor.svr_regressor
                   ] #Models all have the same parameters
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


results = []
models = []
for model in model_functions:
    name,mdl,mse,mae,r_squared = model(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test,X=X,y=y)
    results.append([name,mse,mae,r_squared])
    
    if r_squared is not None:
        models.append((name,mdl))

voter_model = VotingRegressor(estimators=models)
voter_model.fit(X, y)
voter_pred = voter_model.predict(X_test)
r_squared = voter_model.score(X, y)
mse = mean_squared_error(y_test, voter_pred)
mae = mean_absolute_error(y_test, voter_pred)
results.append(["Voter",mse,mae,r_squared])

if prediction_year is not None:
    prediction = predict.predict(str(prediction_year),voter_model)
    print(prediction)
    pd.DataFrame(prediction, columns=["Id", "Year", "Game", "GameNum", "Result"]).to_csv(f'evaluation/{prediction_year}_tournament_results.csv', index=False)

pd.DataFrame(results,columns=["Name","MSE","MAE","R-Squared"]).to_csv(r'evaluation\results.csv')