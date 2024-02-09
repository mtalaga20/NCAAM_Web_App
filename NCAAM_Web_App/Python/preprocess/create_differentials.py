'''
Code to create differential in data. Differentials will be the +/- between the team and their oponents where the data is ()
Part A - Before combining differentials
1. Differential for basic stats
2. Differential for advanced stats
3. Combine differentials into one file
'''

import pandas as pd
import numpy as np

def create_differentials(year:str, root:str):
# -- PART A -- #
    csv_path = root + r'Python\\CSV_Data\\'
        
    basic = pd.read_csv(csv_path+f'{year}\\basic.csv')
    basic_opp = pd.read_csv(csv_path+f'{year}\\basic_opp.csv')
    adv = pd.read_csv(csv_path+f'{year}\\adv.csv')
    adv_opp = pd.read_csv(csv_path+f'{year}\\adv_opp.csv')

    #Column pre-processing

    basic_matrix = basic.to_numpy()
    basic_opp_matrix = basic_opp.to_numpy()
    basic_dif_matrix = np.empty(shape=[0,len(basic.columns)])
    adv_matrix = adv.to_numpy()
    adv_opp_matrix = adv_opp.to_numpy()
    adv_dif_matrix = np.empty(shape=[0,len(adv.columns)])
    #Combine
    for i in range(basic_matrix.shape[0]):
        dif_data = []
        adv_dif_data = []
        for j in range((basic_matrix[i].shape[0])):
            if j < 22:
                dif_data.append(basic_matrix[i][j])
                adv_dif_data.append(adv_matrix[i][j])
            else:
                dif_data.append(basic_matrix[i][j] - basic_opp_matrix[i][j])
                if j <= 33:
                    adv_dif_data.append(adv_matrix[i][j] - adv_opp_matrix[i][j])
        basic_dif_matrix = np.vstack((basic_dif_matrix, np.array(dif_data)))
        adv_dif_matrix = np.vstack((adv_dif_matrix, (np.array(adv_dif_data))))

    #Output results as CSV
    basic_df = pd.DataFrame(basic_dif_matrix, columns=basic.columns)
    basic_df = basic_df.loc[:,~basic_df.columns.str.match("Unnamed")] #Remove empty columns
    basic_df['School'] = basic_df.School.str.replace(u"\u00A0" , ' ')
    basic_df['School'] = basic_df.School.str.replace(' NCAA' , '')
    basic_df.to_csv(csv_path + f'{year}\\basic_differential.csv', index=False)

    adv_dif = pd.DataFrame(adv_dif_matrix, columns=adv.columns)
    adv_dif = adv_dif.loc[:,~adv_dif.columns.str.match("Unnamed")]
    adv_dif['School'] = adv_dif.School.str.replace(u"\u00A0" , ' ')
    adv_dif['School'] = adv_dif.School.str.replace(' NCAA' , '')

    adv_dif.to_csv(csv_path + f'{year}\\adv_differential.csv', index=False)
    return None