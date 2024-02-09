'''
Code to rank the teams in a year
'''

import pandas as pd
import pickle
import warnings
from platform import python_version
from modeling import gradient_boost_regressor
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import train_test_split 

warnings.filterwarnings("ignore")

#----------------------------------------------
prediction_year = None #year or None
#----------------------------------------------
root = 'NCAAM_Web_App\\'
csv_path = r'Python\\CSV_Data\\'
beginning_year = 2010
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023]
if prediction_year is not None: years.remove(prediction_year)
model_functions = [gradient_boost_regressor.gb_regressor
                   ] #Models all have the same parameters

#Train
df = pd.read_csv(root + csv_path+f'{beginning_year}\\{beginning_year}_data.csv')
df = df.iloc[:,2:]
for year in years:
    small_df = pd.read_csv(root + csv_path+f'{year}\\{year}_data.csv')
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

with open(root + f'Python/modeling/best-model{python_version()}.pkl','wb') as f:
    pickle.dump(voter_model,f)
    print("Model saved.")