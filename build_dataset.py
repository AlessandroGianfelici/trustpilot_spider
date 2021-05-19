# -*- coding: utf-8 -*-
import pandas as pd
import os

path = 'data'
mylist = []
for file in os.listdir('data'):
    tmp = pd.read_csv(os.path.join('data', file))
    mylist.append(tmp.loc[tmp['language'] == 'it'])
    
result = pd.concat(mylist)[['company_name','review_title','review_text','review_stars']].drop_duplicates()
print(f"Dumping {len(result}) results...")
result.to_csv('data.csv', index=0)
print("Done!")
