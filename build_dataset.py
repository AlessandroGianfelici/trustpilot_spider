# -*- coding: utf-8 -*-
import pandas as pd
import os

path = 'data'
mylist = []
all_files = os.listdir('data')
print(f"Found {len(all_files)} files...")

for file in :
    tmp = pd.read_csv(os.path.join('data', file))
    mylist.append(tmp.loc[tmp['language'] == 'it'])
    
result = pd.concat(mylist)[['company_name','review_title','review_text','review_stars']].drop_duplicates()
print(f"Dumping {len(result)} reviews...")
result.to_csv('data.csv', index=0)
print("Done!")
