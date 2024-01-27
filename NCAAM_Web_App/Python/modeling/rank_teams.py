'''
Code to run the best model and rank all the teams
'''

#import pyodbc
import math
import pandas as pd
import numpy as np
import warnings
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import Table, Column, Integer, String
from modeling import gradient_boost_regressor
from utility import sqlServerConnect
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")

def rank_teams(prediction_year:str) -> None:
    #----------------------------------------------
    #prediction_year = 2024 #year or None
    #----------------------------------------------

    #cursor = sqlServerConnect.connect()
    csv_path = r'Python\\CSV_Data\\'
    beginning_year = 2010
    years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023,2024]
    if prediction_year is not None: years.remove(prediction_year)
    model_functions = [gradient_boost_regressor.gb_regressor
                    ] #Models all have the same parameters

    #Train
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

    COACH_COLUMNS = 10 #Fixed int

    basic_dif = pd.read_csv(csv_path + f'{prediction_year}\\basic_differential.csv')
    adv_dif = pd.read_csv(csv_path + f'{prediction_year}\\adv_differential.csv')
    conferences = pd.read_csv(csv_path+'\\conferences.csv') 
    coach = pd.read_csv(csv_path+f'{prediction_year}\\coach.csv')
    coach = coach.fillna(0)
    ratings = pd.read_csv(csv_path+f'{prediction_year}\\ratings.csv')
    ratings = ratings.fillna(0)
    column_size = len(basic_dif.columns)+len(adv_dif.columns)
    final_dif = np.empty(shape=[0,COACH_COLUMNS+column_size-1])
    teams = []

    remove_teams = ['Chicago State', 'Hartford', 'Illinois-Chicago', 'Southern Methodist'
                        , 'Youngstown State', 'Abilene Christian', 'Southern Mississippi'] #NOTE bad teams
    all_teams = basic_dif['School'].to_list()
    all_teams = [i for i in all_teams if i not in remove_teams]
    total = len(all_teams) - 1

    #Play all teams
    for i in range(basic_dif.shape[0] - len(remove_teams)):
        away_team = all_teams[i]
        conference = conferences.loc[conferences['Team'] == away_team]['Conference'].item() if away_team in conferences['Team'].values else '-'
        away_basic = basic_dif.loc[basic_dif['School'] == away_team].to_numpy().flatten()
        away_adv = adv_dif.loc[adv_dif['School'] == away_team].to_numpy().flatten()
        away_coach = coach.loc[coach['School'] == away_team].to_numpy().flatten()
        away_ratings = ratings.loc[ratings['School'] == away_team].to_numpy().flatten()

        wins = 0
        for j in range(basic_dif.shape[0] - len(remove_teams)):
            if j == i:
                continue
            home_team = all_teams[j]
            home_basic = basic_dif.loc[basic_dif['School'] == home_team].to_numpy().flatten()
            home_adv = adv_dif.loc[adv_dif['School'] == home_team].to_numpy().flatten()
            home_coach = coach.loc[coach['School'] == home_team].to_numpy().flatten()
            home_ratings = ratings.loc[ratings['School'] == home_team].to_numpy().flatten()

            new_row = []
            #new_row = [away_team, home_team]
            for z in range(2, (column_size-2)):
                if z<len(basic_dif.columns):
                    new_row.append(home_basic[z]-away_basic[z])
                else:
                    new_row.append(home_adv[z-len(basic_dif.columns)+2] - away_adv[z-len(basic_dif.columns)+2])

            #Coach stats
            new_row.append(home_coach[14]-away_coach[14])
            new_row.append(home_coach[15]-away_coach[15])
            new_row.append(home_coach[16]-away_coach[16])
            new_row.append(home_coach[17]-away_coach[17])
            new_row.append(home_coach[18]-away_coach[18])
            new_row.append(home_coach[22]-away_coach[22])
            new_row.append(home_coach[23]-away_coach[23])
            new_row.append(home_coach[24]-away_coach[24])
            new_row.append(home_coach[25]-away_coach[25])
            new_row.append(int(home_coach[26])-int(away_coach[26]))
            #Rating Stats
            new_row.append(home_ratings[12]-away_ratings[12]) #OSRS
            new_row.append(home_ratings[13]-away_ratings[13]) #DSRS
            new_row.append(home_ratings[16]-away_ratings[16]) #DRtg
            
            new_row = [0 if math.isnan(i) else i for i in new_row] 

            pred = voter_model.predict([new_row])[0]

            if pred < 0:
                wins += 1

        teams.append({"Team": away_team, "Wins": wins, "Conference": conference, "W": away_ratings[5], "L": away_ratings[6],
                      "SRS": away_ratings[15], "AP": int(away_ratings[4]), "OSRS": away_ratings[13],
                      "DSRS": away_ratings[14]})

    teams = sorted(teams, key=lambda i: i['Wins'], reverse=True)
    rows = []
    for i in range(len(teams)):
        rows.append([i+1, teams[i]["Team"], teams[i]["Wins"], teams[i]["Conference"], teams[i]["W"], teams[i]["L"], teams[i]["SRS"],
                     teams[i]["AP"], teams[i]["OSRS"], teams[i]["DSRS"]])

    df = pd.DataFrame(rows, columns=['Ranking', 'TeamName', 'Score', 'Conference', 'W', 'L', 'SRS', 'APRank', 'OSRS', 'DSRS'])
    df.to_csv(f'evaluation/{prediction_year}_rankings.csv', index=False)

    #Add to database
    engine = create_engine('mssql+pyodbc://.\SQLEXPRESS/NCAAM_Stats?trusted_connection=yes&driver=SQL+Server', use_setinputsizes=False)
    
    try:
        df.to_sql("Rank", engine, if_exists="replace")
        #df.to_sql("Rank", engine, if_exists="replace", dtype={'Ranking': Integer, 'TeamName': String(collation='utf8'), 
        #                                                      'Score': Integer, 'Conference': String(collation='utf8')})
    except Exception as e:
        print(e)