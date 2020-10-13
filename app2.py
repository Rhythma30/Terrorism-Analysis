# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:52:07 2020

@author: user
"""

import pandas as pd
def main():
    print("Welcome")
    dataset_name = 'global_terror1.csv'
    df = pd.read_csv(dataset_name)
    df.columns.tolist()
    df['nkill'].fillna(0,inplace=True)
    filter_1 = (df['country_txt']=='India')
    df1=df[filter_1]
    df1.to_csv(r'C:\Users\user\Desktop\MLProject\india_terror1.csv',header=True,index = False)
    
               
    
    
    
    
    
    
    
if(__name__ == '__main__'):
    main()
    