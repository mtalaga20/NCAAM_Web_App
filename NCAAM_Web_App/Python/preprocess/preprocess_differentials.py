'''
Part B
Code to pre-process differentials

For basic stats
- Convert W/L totals to a ratio
- Divide points by games played to make PPG column

For advanced stats
- Remove redundant columns
'''

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def preprocess_differentials(year:str, root:str):
    csv_path = root + r'Python\\CSV_Data\\'

    #Conference Pre-process
    teams = pd.read_csv(csv_path+'teams.csv')
    big_ten = teams.loc[teams['Conference'] == 'Big 10']['School'].to_numpy().tolist()
    acc = teams.loc[teams['Conference'] == 'ACC']['School'].to_numpy().tolist()
    big_east = teams.loc[teams['Conference'] == 'Big East']['School'].to_numpy().tolist()
    big_twelve = teams.loc[teams['Conference'] == 'Big 12']['School'].to_numpy().tolist()
    sec = teams.loc[teams['Conference'] == 'SEC']['School'].to_numpy().tolist()
    blueblood = ['Duke','North Carolina','Kentucky','UCLA','Kansas','Indiana']

    #Basic stats pre-processing
    basic_dif = pd.read_csv(csv_path+f'{year}\\basic_differential.csv')
    #try:
    basic_dif['PPG'] = (basic_dif['Tm.'] - basic_dif['Opp.']) // basic_dif['G']
    basic_dif['Big10'] = basic_dif['School'].isin(big_ten).astype(int)
    basic_dif['Big12'] = basic_dif['School'].isin(big_twelve).astype(int)
    basic_dif['ACC'] = basic_dif['School'].isin(acc).astype(int)
    basic_dif['SEC'] = basic_dif['School'].isin(sec).astype(int)
    basic_dif['BigEast'] = basic_dif['School'].isin(big_east).astype(int)
    basic_dif['BlueBlood'] = basic_dif['School'].isin(blueblood).astype(int)
    basic_dif['Championships'] = 0
    for i in range(basic_dif.shape[0]):
        try:
            basic_dif['Championships'][i] = teams.loc[teams['School'] == basic_dif['School'][i]]['Championships'].iloc[0]
        except:
            pass
    basic_dif['Conf_W-L%'] = (basic_dif['W.1'] / (basic_dif['W.1'] + basic_dif['L.1']))
    basic_dif['Home_W-L%'] = (basic_dif['W.2'] / (basic_dif['W.2'] + basic_dif['L.2']))
    basic_dif['Away_W-L%'] = basic_dif['W.3'] / (basic_dif['W.3'] + basic_dif['L.3'])
    basic_dif['3P-G'] = basic_dif['3P'] / basic_dif['G']
    basic_dif['3PA-G'] = basic_dif['3PA'] / basic_dif['G']
    basic_dif['FG-G'] = basic_dif['FG'] / basic_dif['G']
    basic_dif['FGA-G'] = basic_dif['FGA'] / basic_dif['G']
    basic_dif['FT-G'] = basic_dif['FT'] / basic_dif['G']
    basic_dif['FTA-G'] = basic_dif['FTA'] / basic_dif['G']
    basic_dif['ORB-G'] = basic_dif['ORB'] / basic_dif['G']
    basic_dif['TRB-G'] = basic_dif['TRB'] / basic_dif['G']
    basic_dif['AST-G'] = basic_dif['AST'] / basic_dif['G']
    basic_dif['STL-G'] = basic_dif['STL'] / basic_dif['G']
    basic_dif['BLK-G'] = basic_dif['BLK'] / basic_dif['G']
    basic_dif['TOV-G'] = basic_dif['TOV'] / basic_dif['G']
    basic_dif['PF-G'] = basic_dif['PF'] / basic_dif['G']
    basic_dif.drop(['W','L','W.1','L.1','W.2','L.2','W.3','L.3','Tm.','Opp.','3P','FT','FTA','FG','FGA','MP',
                    'ORB','TRB','AST','STL','BLK','TOV','PF','G'], axis=1, inplace=True)

    #Advanced Stats pre-processing
    adv_dif = pd.read_csv(csv_path+f'{year}\\adv_differential.csv')
    if adv_dif.columns[0] == 'Rk':
        cols = [x for x in range(2,16)]
        adv_dif.drop(adv_dif.columns[cols],axis=1,inplace=True)
        adv_dif.to_csv(csv_path+f'{year}\\adv_differential.csv', index=False)
    else:
        print(f'Year {year} has already been preprocessed or is not formatted correctly.')
    
    basic_dif.to_csv(csv_path+f'{year}\\basic_differential.csv', index=False)
    return None
        