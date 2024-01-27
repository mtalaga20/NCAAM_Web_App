'''
'''
import pandas as pd 
import math

def predict(year:str,model):
    csv_path = r'CSV_Data\\'
    game_map = pd.read_csv(csv_path+'game_map.csv')
    games = pd.read_csv(csv_path + f'{year}\\new_tourney.csv').to_numpy().tolist()
    basic_dif = pd.read_csv(csv_path + f'{year}\\basic_differential.csv')
    adv_dif = pd.read_csv(csv_path + f'{year}\\adv_differential.csv')
    coach = pd.read_csv(csv_path+f'{year}\\coach.csv')
    coach = coach.fillna(0)
    ratings = pd.read_csv(csv_path+f'{year}\\ratings.csv')
    ratings = ratings.fillna(0)

    column_size = len(basic_dif.columns)+len(adv_dif.columns)
    #final_dif = np.empty(shape=[0,column_size-2])
    complete = False
    log = []
    count = 1

    while not complete:
        away_team = games[0][0]
        game = games[0][1]
        
        #try:
        if True:
            for i in range(1,len(games)):
                if(games[i][1]==game):
                    home_team = games[i][0]
                    home_index = i
                    break

            away_basic = basic_dif.loc[basic_dif['School'] == away_team].to_numpy().flatten()
            away_adv = adv_dif.loc[adv_dif['School'] == away_team].to_numpy().flatten()
            away_coach = coach.loc[coach['School'] == away_team].to_numpy().flatten()
            away_ratings = ratings.loc[ratings['School'] == away_team].to_numpy().flatten()
            try:
                home_basic = basic_dif.loc[basic_dif['School'] == home_team].to_numpy().flatten()
            except:
                print('Completed predictions')
            home_adv = adv_dif.loc[adv_dif['School'] == home_team].to_numpy().flatten()
            home_coach = coach.loc[coach['School'] == home_team].to_numpy().flatten()
            home_ratings = ratings.loc[ratings['School'] == home_team].to_numpy().flatten()


            differential = [] #[away_team, home_team]
            for j in range(2, (column_size-2)):
                if j<len(basic_dif.columns):
                    differential.append(home_basic[j]-away_basic[j])
                else:
                    differential.append(home_adv[j-len(basic_dif.columns)+2] - away_adv[j-len(basic_dif.columns)+2])
            
            #Coach stats
            differential.append(home_coach[14]-away_coach[14])
            differential.append(home_coach[15]-away_coach[15])
            differential.append(home_coach[16]-away_coach[16])
            differential.append(home_coach[17]-away_coach[17])
            differential.append(home_coach[18]-away_coach[18])
            differential.append(home_coach[22]-away_coach[22])
            differential.append(home_coach[23]-away_coach[23])
            differential.append(home_coach[24]-away_coach[24])
            differential.append(home_coach[25]-away_coach[25])
            differential.append(int(home_coach[26])-int(away_coach[26]))

            #Rating Stats
            differential.append(home_ratings[12]-away_ratings[12]) #OSRS
            differential.append(home_ratings[13]-away_ratings[13]) #DSRS
            differential.append(home_ratings[16]-away_ratings[16]) #DRtg

            #replace nan with 0
            for i in range(len(differential)):
                if math.isnan(differential[i]):
                    differential[i] = 0

            pred = model.predict([differential])[0]
            winner = home_team if pred > 0 else away_team
            loser = home_team if winner == away_team else away_team
            #print(f'Game {game} - {winner} beats {loser} by {abs(pred)}')
            log.append([f'{year}.{game}', year, game, count, f'Game {game} - {winner} beats {loser} by {abs(pred)}'])
            count += 1
            games.pop(0)
            games.pop(home_index-1)
            if game != 'Play-in':
                try:
                    next_game = game_map.loc[game_map['Game'] == game]['Next'].to_numpy()[0]
                    if next_game == 'Champion': 
                        complete=True
                        #log+=f'Champion - {winner}'
                    games.append([winner,next_game])
                except Exception as e:
                    print(e)
                    print(f"\nCould not find next game for {winner}")
            print()
                
        #except:
            #complete=True
            #log += f'The winner is {winner}'

    return log
