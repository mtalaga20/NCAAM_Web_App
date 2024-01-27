'''Tests to fetch data as df'''

import pandas as pd
from preprocess import preprocess_data
from modeling import rank_teams
#from sportsreference.nba.teams import Teams #Deprecated
#teams = Teams()
#for team in teams:
#    print(team.name)

###----------------------------------------------------------------------------
#years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023,2024]
#years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022,2023]
years = [2009]
preprocess = True
tourney = True #False #Whether the years all have tournament games (i.e. tourney_games.csv)
#Flags to rank teams - both need to be on for latest year only
rank_tms = False #True
rank_teams_latest_year_only = True
###----------------------------------------------------------------------------

#Number of tables to populate from sports-reference.com
for year in years:
    for i in range(6):
        match i:
            case 0: 
                url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-school-stats.html"
                df = pd.read_html(url, header=1)[0]
                #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
                df.to_csv(f'Python/CSV_Data/{year}/basic.csv', index=False)
            case 1: 
                url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-opponent-stats.html"
                df = pd.read_html(url, header=1)[0]
                #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
                df.to_csv(f'Python/CSV_Data/{year}/basic_opp.csv', index=False)
            case 2: 
                url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-advanced-school-stats.html"
                df = pd.read_html(url, header=1)[0]
                #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
                df.to_csv(f'Python/CSV_Data/{year}/adv.csv', index=False)
            case 3: 
                url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-advanced-opponent-stats.html"
                df = pd.read_html(url, header=1)[0]
                #df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df = df[(df.Rk != '') & (df.Rk != 'Rk') & (df.G != 'Overall')]
                df.to_csv(f'Python/CSV_Data/{year}/adv_opp.csv', index=False)
            case 4:
                url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-coaches.html"
                df = pd.read_html(url, header=1)[0]
                df = df[(df.Coach != '') & (df.Coach != 'Coach') & (df.W != '2023-24 Season')]
                df.to_csv(f'Python/CSV_Data/{year}/coach.csv', index=False)
            case 5:
                url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-ratings.html"
                df = pd.read_html(url, header=1)[0]
                df = df[(df.School != '') & (df.School != 'School') & (df.ORtg != 'Adjusted')]
                df.to_csv(f'Python/CSV_Data/{year}/ratings.csv', index=False)

    if preprocess:
        #Preprocess dfs
        preprocess_data.preprocess([year], tourney)

    if rank_tms:
        #Update rankings
        if rank_teams_latest_year_only and year != years[-1]:   
            continue
        rank_teams.rank_teams(int(year))

print("Completed")