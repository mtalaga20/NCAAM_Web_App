'''
Simple models to train and test with
'''

import pandas as pd 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from keras.models import Sequential
from keras.layers import Dense


def nn_regressor(X_train:pd.DataFrame,X_test:pd.DataFrame,y_train:pd.DataFrame,
                     y_test:pd.DataFrame,X:pd.DataFrame,y:pd.DataFrame):
    name = "Neural Net"

    #Train
    input_size = len(X_train.columns)
    model = Sequential()
    model.add(Dense(500, input_dim=input_size, activation= "relu"))
    model.add(Dense(100, activation= "relu"))
    model.add(Dense(50, activation= "relu"))
    model.add(Dense(1))

    model.compile(loss= "mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])
    model.fit(X_train, y_train, epochs=16)
    predictions = model.predict(X_test)
    r_squared = None
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    print(f"\n--- {name} ---")
    print( 
    'mean_squared_error : ', mean_squared_error(y_test, predictions)) 
    print( 
    'mean_absolute_error : ', mean_absolute_error(y_test, predictions))

    return  name,model,mse,mae,r_squared