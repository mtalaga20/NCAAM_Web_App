'''
Simple models to train and test with
'''

import pandas as pd 
import numpy as np 
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from sklearn.metrics import mean_squared_error, mean_absolute_error 

def gaussian_process_regressor(X_train:pd.DataFrame,X_test:pd.DataFrame,y_train:pd.DataFrame,
                     y_test:pd.DataFrame,X:pd.DataFrame,y:pd.DataFrame):
  name = "Gaussian Process Regressor"

  #Regression
  kernel = DotProduct() + WhiteKernel()
  model = GaussianProcessRegressor(kernel=kernel,random_state=0) 
  model.fit(X_train,y_train)
  predictions = model.predict(X_test)
  r_squared = model.score(X, y)
  mse = mean_squared_error(y_test, predictions)
  mae = mean_absolute_error(y_test, predictions)

  print(f"\n---{name} ---")
  print( 
    'mean_squared_error : ', mean_squared_error(y_test, predictions)) 
  print( 
    'mean_absolute_error : ', mean_absolute_error(y_test, predictions))
  print(
      'R2: ', r_squared
  ) 

  return name,model,mse,mae,r_squared