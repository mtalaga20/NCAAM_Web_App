import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = r'C:\Users\mktal\repos\College_Basketball_Game_Prediction\CSV_Data\\'

df = pd.read_csv(csv_path+f'2023\\2023_data.csv')
df = df.iloc[:,2:]

for year in [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022]:
    small_df = pd.read_csv(csv_path+f'{year}\\{year}_data.csv')
    small_df = small_df.iloc[:,2:]
    df = pd.concat([df,small_df])

matrix = df.corr().round(4)
sns.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
#plt.show()
top25 = matrix.sort_values('Score_Dif', ascending=False)['Score_Dif'].head(25)
top25_ascending = matrix.sort_values('Score_Dif')['Score_Dif'].head(25)
print(top25)
