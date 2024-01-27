'''
Part C
1. Take games and score result and combine differentials for two teams to form one differential
'''

import pandas as pd
import numpy as np

def combine_differentials(year:str):
    # -- PART C -- #
    COACH_COLUMNS = 10 #Fixed int
    RATING_COLUMNS = 3

    csv_path = r'Python\\CSV_Data\\'
    #for year in [2015,2016,2017,2018,2019,2021,2022,2023]:
    games = pd.read_csv(csv_path + f'{year}\\tourney_games.csv').to_numpy()
    basic_dif = pd.read_csv(csv_path + f'{year}\\basic_differential.csv')
    adv_dif = pd.read_csv(csv_path + f'{year}\\adv_differential.csv')
    
    coach = pd.read_csv(csv_path+f'{year}\\coach.csv') 
    coach = coach.fillna(0)
    ratings = pd.read_csv(csv_path+f'{year}\\ratings.csv') 
    ratings = ratings.fillna(0)

    column_size = len(basic_dif.columns)+len(adv_dif.columns)
    final_dif = np.empty(shape=[0,COACH_COLUMNS+RATING_COLUMNS+column_size-1])

    for i in range(games.shape[0]):
        away_team = games[i][0]
        home_team = games[i][1]
        score_differential = games[i][2] #Differential favors home team where it is (home points - away points)

        away_basic = basic_dif.loc[basic_dif['School'] == away_team].to_numpy().flatten()
        away_adv = adv_dif.loc[adv_dif['School'] == away_team].to_numpy().flatten()
        away_coach = coach.loc[coach['School'] == away_team].to_numpy().flatten()
        away_rating = ratings.loc[ratings['School'] == away_team].to_numpy().flatten()

        home_basic = basic_dif.loc[basic_dif['School'] == home_team].to_numpy().flatten()
        home_adv = adv_dif.loc[adv_dif['School'] == home_team].to_numpy().flatten()
        home_coach = coach.loc[coach['School'] == home_team].to_numpy().flatten()
        home_rating = ratings.loc[ratings['School'] == home_team].to_numpy().flatten()

        new_row = [away_team, home_team]
        for j in range(2, (column_size-2)):
            if j<len(basic_dif.columns):
                new_row.append(home_basic[j]-away_basic[j])
            else:
                new_row.append(home_adv[j-len(basic_dif.columns)+2] - away_adv[j-len(basic_dif.columns)+2])

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
        new_row.append(home_rating[12]-away_rating[12]) #OSRS
        new_row.append(home_rating[13]-away_rating[13]) #DSRS
        new_row.append(home_rating[16]-away_rating[16]) #DRtg

        new_row.append(score_differential)
        final_dif = np.vstack((final_dif, np.array(new_row)))
        
    
    columns = ["Away","Home"]
    columns.extend(basic_dif.columns[2:])
    columns.extend(adv_dif.columns[2:])

    #Coach columns
    columns.extend(["Coach W/L","Coach Team NCAA","Coach Team S16","Coach Team F4","Coach Team Champs",
                    "Coach C W/L","Coach C NCAA","Coach C S16","Coach C F4","Coach C Champs"]) 
    
    #Ratings Columns
    columns.extend(["OSRS", "DSRS", "DRtg"])

    columns.extend(["Score_Dif"])

    df = pd.DataFrame(final_dif, columns=columns)
    df.to_csv(csv_path + f'{year}\\{year}_data.csv', index=False)
    return None
        