# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:19:13 2020

@author: user
"""

import pandas as pd

if __name__ == '__main__':
    dataset_name = 'globalterrorismdb_0919dist.xlsx'
    selected_columns = [1,2,3,7,8,9,10,11,12,13,14,28,29,34,35,40,41,58,81,82,98,105,106]
    df = pd.read_excel(dataset_name, usecols = selected_columns)
    type(df)
    df.ndim
    df.shape
    df.columns
    print(df.columns)
    df.columns.tolist()
    my_list = df.columns.tolist()
    df.to_csv(r'C:\Users\user\Desktop\MLProject\global_terror1.csv',header=True,index = False)
    print("Kuch toh ho rha hai mtlb")