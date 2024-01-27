'''
'''

import pandas as pd
import numpy as np

# -- PART B-2 -- #

def preprocess_coaches(year:str):
    csv_path = r'Python\\CSV_Data\\'

    coach_team_map = pd.read_csv(csv_path+"coach_team_map.csv")
    coach_team_map = pd.Series(
        coach_team_map['Mapped_Name'].values,
        index=coach_team_map['Team_Name']
    ).to_dict()
    
    coach = pd.read_csv(csv_path+f'{year}\\coach.csv')
    change = coach.replace({"School":coach_team_map})
    change.to_csv(csv_path+f'{year}\\coach.csv', index=False)
    
    ratings = pd.read_csv(csv_path+f'{year}\\ratings.csv')
    change = ratings.replace({"School":coach_team_map})
    change.to_csv(csv_path+f'{year}\\ratings.csv', index=False)
    
    return None