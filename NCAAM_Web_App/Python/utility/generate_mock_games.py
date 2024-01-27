'''
Functions to add more data based on learned data
'''
import pandas as pd
import numpy as np

def generate_mock_data(year, matchups):
    csv_path = r'CSV_Data\\'

    basic_dif = pd.read_csv(csv_path + f'{year}\\basic_differential.csv')
    adv_dif = pd.read_csv(csv_path + f'{year}\\adv_differential.csv')
    column_size = len(basic_dif.columns)+len(adv_dif.columns)
    final_dif = np.empty(shape=[0,column_size-2])

    for i in range(matchups.shape[0]):
        away_team = matchups.iloc[i,0]
        home_team = matchups.iloc[i,1]
        away_basic = basic_dif.loc[basic_dif['School'] == away_team].to_numpy().flatten()
        away_adv = adv_dif.loc[adv_dif['School'] == away_team].to_numpy().flatten()
        home_basic = basic_dif.loc[basic_dif['School'] == home_team].to_numpy().flatten()
        home_adv = adv_dif.loc[adv_dif['School'] == home_team].to_numpy().flatten()

        new_row = [away_team, home_team]
        for j in range(2, (column_size-2)):
            if j<len(basic_dif.columns):
                new_row.append(home_basic[j]-away_basic[j])
            else:
                new_row.append(home_adv[j-len(basic_dif.columns)+2] - away_adv[j-len(basic_dif.columns)+2])
                
        final_dif = np.vstack((final_dif, np.array(new_row)))

        columns = ["Away","Home"]
        columns.extend(basic_dif.columns[2:])
        columns.extend(adv_dif.columns[2:])

        df = pd.DataFrame(final_dif, columns=columns)
    
    return df
