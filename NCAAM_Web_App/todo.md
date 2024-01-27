## Pre-processing and Data
- [x] Collect data for all years
- [x] Get score for all years
- [x] Calculate differential files
- [x] Develop a way to update existing data automatically
  - [x] Scrape data
  - [x] Automatically run pre-processing after scrape (schedule)
- [x] Scrape bracketology teams

## Analysis
- [x] Do a correlation analysis to determine the most relevant features

## Modeling
- [x] Split the data into train/test/split
- [x] Create a prediction output
- [x] Create a model to rank all the teams in the data (sort)
- [x] Make a model that doesn't depend on training to be run (like team versus)

## Web Application
- [x] Create a versus option
- [x] Create a page for ranking
- [] Create a page to add a bracket
- [] Add W/L to rankings, SRS? 
- [] Have a home page that explains the model, best stats, and limitations/results

### App pages
- Rankings list (update button)
- Bracket games
### Database Tables
Rankings - team name (unique), path for image if available, rank nbr, week nbr?
Sim bracket (optional)