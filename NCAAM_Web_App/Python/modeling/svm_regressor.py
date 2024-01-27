'''
Not yet functional
'''

import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sklearn.svm import SVR

 
def svr_regressor(X_train:pd.DataFrame,X_test:pd.DataFrame,y_train:pd.DataFrame,
                     y_test:pd.DataFrame,X:pd.DataFrame,y:pd.DataFrame):
    name = "SVM Regressor"
    regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
    regr.fit(X,y)
    model = SVR(kernel = 'rbf')
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