'''
Pre-process data and create data files for each year
'''

from preprocess import combine_differentials
from preprocess import create_differentials
from preprocess import preprocess_coaches
from preprocess import preprocess_differentials

#years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2021','2022','2023']
def preprocess(years:list[int], tourney = False) -> None:
    for year in years:
        #Preprocess coach data
        preprocess_coaches.preprocess_coaches(year)
        #Create differentials between team and opposition data
        create_differentials.create_differentials(year)
        #Preprocess differentials
        preprocess_differentials.preprocess_differentials(year)
        
        if tourney:
            #Combine differentials for tourney games between teams playing
            combine_differentials.combine_differentials(year)