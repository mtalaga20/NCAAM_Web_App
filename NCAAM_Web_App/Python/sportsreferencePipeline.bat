'''Tests to fetch data as df'''

import pandas as pd
from preprocess import preprocess_data
from modeling import rank_teams
#from sportsreference.nba.teams import Teams #Deprecated
#teams = Teams()
#for team in teams:
#    print(team.name)

###----------------------------------------------------------------------------
year = '2024'
###----------------------------------------------------------------------------
url = "https://www.sports-reference.com/cbb/seasons/men/2024-school-stats.html"

#Number of tables to populate from sports-reference.com
for i in range(5):
    match i:
        case 0: 
            url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-school-stats.html"
            df = pd.read_html(url, header=1)[0]
            #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
            df.to_csv(f'CSV_Data/{year}/basic.csv', index=False)
        case 1: 
            url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-opponent-stats.html"
            df = pd.read_html(url, header=1)[0]
            #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
            df.to_csv(f'CSV_Data/{year}/basic_opp.csv', index=False)
        case 2: 
            url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-advanced-school-stats.html"
            df = pd.read_html(url, header=1)[0]
            #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
            df.to_csv(f'CSV_Data/{year}/adv.csv', index=False)
        case 3: 
            url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-advanced-opponent-stats.html"
            df = pd.read_html(url, header=1)[0]
            #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
            df.to_csv(f'CSV_Data/{year}/adv_opp.csv', index=False)
        case 4:
            url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-coaches.html"
            df = pd.read_html(url, header=1)[0]
            df = df[(df.Coach != '') & (df.Coach != 'Coach') & (df.W != '2023-24 Season')]
            df.to_csv(f'CSV_Data/{year}/coach.csv', index=False)

#Preprocess dfs
preprocess_data.preprocess([year])

#Update rankings
rank_teams.rank_teams(int(year))

print("Completed")