# College_Basketball_Tournament_Game_Prediction
This code is created to automate and train on NCAA Men's basketball data for team rankings and game prediction. Data is used from sports-reference.com . It is trained on historical data from March Madness games (manually pulled from ESPN). Please use at your own risk. This model is not responsible for anything you do with the information and does not guarantee outcomes of games. Several limitations do exist and are areas for improvement. Firstly, streaky teams are not considered. The entire season is reflected in the data used and is a general scope of the team. Additionally, injuries are not considered, which can help or hinder a team's potential. Personal performance is not a metric, and player height is not considered, which is something that I wish to include at some point.

# Requirements
- Python 3.11.x version and packages listed in requirements.txt
- SQL Server and SSMS

# Getting Started
1. SQL Server Setup - This code base requires a SQL server database. You can change the names in the code, but I have named the database NCAAM_Stats.
2. The data is already pre-processed for training the model. To train a model, you can run run_model.py to save a .pkl file of a model. There are multiple models that can be used in a Voting Regressor, but gradient boost performed the best. Do this step before proceeding.
3. Task Scheduler Setup - Schedule the file named sportsreferencePipeline.py to be run daily to update the database. This will scrape data from sports-reference.com and pre-process it. It is set for the current season of 2024, which can be changed in the script.
4. Run the .NET web application to view and filter the data. Code is at https://github.com/mtalaga20/NCAAM_Web_App.

# Functionality



### Bracket
W      -      S

E      -      MW

##Linear Correlation Results
### Positive Correlation
|Rank |Category|Score   | Calculation  |
|---|---|---|---|
| 1  | SRS   | 0.56  |  Average point differential and strength of schedule |
| 2  | SOS - Strenth of Schedule  | 0.41  | |
| 3  | DSRS - Defense SRS  | 0.35  | |
| 4  | PPG  | 0.34  | |
| 5  | OSRS - Offensive SRS  | 0.32  | |
| 6  | FG/G  | 0.28  | |
| 7  | W/L %  | 0.27  | |
| 8  | Coach Conference W/L %  | 0.26  | |
| 9  | Coach W/L %  | 0.24  | |
| 10  | Coach Sweet 16 App  | 0.24  | |
| 11  | Coach NCAA App  | 0.22  | |
| 12  | Efficient FG %  | 0.21  |(FG + 0.5 * 3P) / FGA |

### Negative Correlation
|Rank |Category|Score   | Calculation  |
|---|---|---|---|
| 1  | PACE - Number of possesions  | -0.11  | 40 * (Poss / (0.2 * Tm MP))  |
| 2  | FTr  | -0.10  | |
| 3  | TS% - True Shoot Percentage (with free throws) | -0.07  |PTS / (2 * (FGA + 0.475 * FTA)) |
