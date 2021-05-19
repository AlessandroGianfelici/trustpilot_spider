# -*- coding: utf-8 -*-
import pandas as pd
import os

path = 'data'
mylist = []
for file in os.listdir('data'):
    tmp = pd.read_csv(os.path.join('data', file))
    mylist.append(tmp.loc[tmp['language'] == 'it'])
    
pd.concat(mylist).to_csv('data.csv', index=0)
    
