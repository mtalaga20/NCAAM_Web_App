import pandas as pd
import requests
import json
import string
from platform import python_version
import re
import pickle
from bs4 import BeautifulSoup as bs
from pandas.io.json import json_normalize
from modeling import team_versus_fcn

#Needed to use python 3.7
###----------------------------------------------------------------------------
year = '2024'
regions = ["MIDWEST (DETROIT)", "EAST (BOSTON)", "SOUTH (DALLAS)", "WEST (LOS ANGELES)"]
locations = ["BROOKLYN", "PITTSBURGH", "CHARLOTTE", "SALT LAKE", "OMAHA",
             "SPOKANE", "CHARLOTTE", "MEMPHIS", "INDIANAPOLIS"]
###----------------------------------------------------------------------------

url = r"https://www.espn.com/espn/feature/story/_/page/bracketology/ncaa-bracketology-2024-march-madness-men-field-predictions"
r = requests.get(url,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})
soup = bs(r.content, 'lxml')
s = soup.select('html')[0].text
#s = '\n\n\n\n\n\nNCAA Bracketology - 2024 March Madness men\'s field predictions\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nESPN0\n0\n0\n\n\n\n\n\n\n\n2024 NCAA Tournament BracketologyBy Joe Lunardi Updated: 1/5/2024 at 6:30 a.m. ETBracketology is now in its 30th season on ESPN.com. From now until Selection Sunday on March 17, we\'ll keep you up to date on the postseason chances and projection of your favorite teams. Our brackets will update Tuesday and Friday now that teams have started conference play. We will culminate with daily updates throughout Championship Week in March, all with an eye toward the 2024 NCAA men\'s basketball tournament. Bracket WatchTop Overall SeedPurdueFirst Team OutTCULast Team InNorthwesternRarely in bracketology is a head-to-head result determinative when it comes to seeding. In this update, however, a single December contest is the dividing line for the final No. 2 seed. Clemson\'s loss at Miami opened the spot, with both Kentucky and North Carolina next in line to move up. It\'s a very close call numerically, but the Wildcats edged the Tar Heels on a neutral court last month and we\'re using that to break the evaluation "tie." It\'s Kentucky Blue that becomes a 2-seed and Carolina Blue holds as a No. 3. In the bigger picture, this Saturday the Big 12 and SEC become the final power conferences to begin league play. It is officially bracket season.On the BubbleLast Four Byes Virginia Utah State South Carolina FloridaLast Four In Texas Nebraska New Mexico NorthwesternFirst Four Out TCU St. John\'s Texas Tech CincinnatiNext Four Out Kansas St. Butler Washington Wake Forest68-Team BracketMoved UpMoved DownNew Team to BracketAutomatic Qualifier16Merrimack16New Mexico St.11Texas11Nebraska16Southern16Stetson12Northwestern12TCUMIDWEST (DETROIT)Indianapolis1 Purdue16 Merrimack - aq/ New Mexico St. - aq8 Ole Miss9 Iowa StateBrooklyn5 Baylor12 Princeton - aq4 Memphis - aq13 Weber St. - aqPittsburgh6 Alabama11 Texas/ Nebraska3 Clemson14 Akron - aqIndianapolis7 Ohio State10 Mississippi St.2 Marquette15 Colgate - aqEAST (BOSTON)Brooklyn1 UConn16 Marist - aq8 Dayton - aq9 MiamiPittsburgh5 Oklahoma12 Indiana St. - aq4 Wisconsin13 Samford - aqSalt Lake6 Creighton11 Grand Canyon - aq3 BYU14 Morehead St. - aqCharlotte7 Michigan St.10 James Madison - aq2 Tennessee - aq15 Vermont - aqSOUTH (DALLAS)Omaha1aq -  Houston16aq -  Southernaq -  Stetson/8 Nevada9 ProvidenceSpokane5 Auburn12 Northwestern TCU/4 Fla. Atlantic13aq -  McNeese St.Charlotte6 Villanova11 Florida3 North Carolina14aq -  High PointMemphis7 Utah10 Utah State2 Kentucky15aq -  DrexelWEST (LOS ANGELES)Omaha1 Kansas16aq -  So. Dakota St.8 Colorado9aq -  GonzagaSpokane5aq -  Colorado St.12aq -  Oregon4 Duke13 UC IrvineMemphis6 San Diego St.11 South Carolina3aq -  Illinois14aq -  Fort WayneSalt Lake7 Texas A&M10 Virginia2 Arizona15aq -  Norfolk St.Conference BreakdownConferenceTeamSEC9Big 127Big Ten7Big East5Mountain West5ACC5Pac-124American2All NCAAM ConferencesPhoto illo by ESPN Illustration, additional photos courtesy of Getty Images, Associated Press, Imagn, USA TODAY Sports, Icon Sportswire, EPA/ShutterstockRelated Stories It\'s about timing? Ranking the current AP-poll men\'s teams by average age College basketball fantasy draft: The 24 best players halfway through the season How men\'s college basketball has played out after one month of action Men\'s Power Rankings: Every team\'s needs to make a deep run this seasonRULESESPN\'s Bracketology efforts are focused on projecting the NCAA tournament field just as we expect the NCAA Division I basketball committee to select the field in March. ESPN bracketologist Joe Lunardi uses the same data points favored by the committee, including strength of schedule and other season-long indicators, including the NET and team-sheet data similar to what is available to the NCAA, in his projections of the field. Visit the NCAA\'s website for a fuller understanding of NCAA selection criteria.68-Team BracketThe 68-team bracket is the standard version of the NCAA tournament field that has been in place since 2011. If the 2021 field is comprised of 68 teams, there will be some key differences to past years, however.The primary adjustment from a normal year is, of course, the playing of the entire NCAA tournament at a single site. This eliminates the need for geographical considerations in seeding. Additionally, there will be at least one fewer automatic qualifier this season, as the Ivy League\'s decision to forgo the 2020-21 season reduces the number of AQ entries to 31 for this season.48-Team BracketIn this projection, a condensed selection process would reduce the field by 10 at-large teams and 10 automatic qualifiers (the latter of which still receive a revenue unit). The top four seeds in each region would receive a bye into the second round, with four first-round games per region - 5 vs. 12, 6 vs. 11, 7 vs. 10 and 8 vs. 9 - being played without fans on the higher seed\'s home court.To minimize travel, first-round pairings will be guided by geography to the greatest extent possible. And the reduced field results in only 32 teams competing at the central site. All participants must post a minimum .500 conference record - the "Lunardi Rule" - for at-large consideration.16-Team BracketIn this projection, the committee selects and seeds the 16 best available teams. There are no automatic qualifiers, although all non-competing conference champions receive the designated revenue unit.To maintain some sense of national balance, conference participation is capped at four teams. And no region shall have more than one team from the same conference.\nMore Stories\n\n\n\n\n\n\nTerms of UsePrivacy PolicyYour US State Privacy RightsChildren\'s Online Privacy PolicyInterest-Based AdsAbout Nielsen MeasurementDo Not Sell or Share My Personal InformationContact UsDisney Ad Sales SiteWork for ESPNCorrections\nCopyright: ® ESPN Enterprises, Inc. All rights reserved.\n\n\n\n\n\n\n\n\n'
x = s.split("BracketAutomatic Qualifier",1)[1].replace(' - aq','').replace('aq -  ', '')
x = x.split("Conference BreakdownConferenceTeam")[0]
for reg in regions:
    x = x.replace(reg, '')
#for loc in locations:
#    x = x.replace(loc, '')
l = re.split('(\d+)', x)
l.remove('')

for i in range(len(l)):
    for loc in locations:
        loc = string.capwords(loc)
        if (loc in l[i]) and (len(l[i]) > len(loc) + 1):
            l[i]=l[i].replace(loc,'')
        
        if ("St. John's" in l[i]):
            l[i]=l[i].replace("St. John's","Saint John's")
        elif ("St. Peter's" in l[i]):
            l[i]=l[i].replace("St. Peter's","Saint Peter's")
        elif('St.' in l[i]):
            l[i]=l[i].replace('St.','State')
        if('So.' in l[i]):
            l[i]=l[i].replace('So.','South')

lranks = l[::2]
lteams = l[1::2]

playins = lteams[:8]
lteams = lteams[8:]
lranks = lranks[8:]
#data= json.loads(s)
#df = pd.read_html(url, header=1)[0]

#Preprocess team names
team_map = pd.read_csv("CSV_Data/coach_team_map.csv")  
team_map = pd.Series(
        team_map['Mapped_Name'].values,
        index=team_map['Team_Name']
    ).to_dict()    

#Make play-ins play each other
with open(f'modeling/best-model{python_version()}.pkl', 'rb') as f:
    model = pickle.load(f)

winners = []
for i in range(0,len(playins),2):
    team_one = playins[i]
    team_two = playins[i+1]

    #Preprocess names
    t1 = team_map[team_one] if team_one in team_map else team_one
    t2 = team_map[team_two] if team_two in team_map else team_two
   
    winner = team_versus_fcn.team_versus(t1, t2, year, model)
    winners.append(team_one if winner==t1 else team_two)

for winner in winners:
    for i in range(len(lteams)):
        if (winner in lteams[i] and r'/' in lteams[i]):
            lteams[i] = winner

for i in range(len(lteams)):
    lteams[i] = lteams[i].strip(' ')

regs = 4
game = 1
for i in range(0,len(lteams),2):
    if regs == 4:
        lteams[i] = [lteams[i], f"W{game}"]
        lteams[i+1] = [lteams[i+1], f"W{game}"]
    elif regs == 3:
        lteams[i] = [lteams[i], f"E{game}"]
        lteams[i+1] = [lteams[i+1], f"E{game}"]
    elif regs == 2:
        lteams[i] = [lteams[i], f"S{game}"]
        lteams[i+1] = [lteams[i+1], f"S{game}"]
    elif regs == 1:
        lteams[i] = [lteams[i], f"MW{game}"]
        lteams[i+1] = [lteams[i+1], f"MW{game}"]
    game +=1
    if game > 8:
        game = 1
        regs -= 1

games = pd.DataFrame(lteams, columns=["Team","Game"])

#Preprocess   
games = games.replace({"Team":team_map})
games.to_csv(f'CSV_Data/{year}/new_tourney.csv', index=False)
#DF