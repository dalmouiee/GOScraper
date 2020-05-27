import pandas as pd
import os

import pandas as pd
df1 = pd.read_csv('Enrich_H_W_Biology.csv').set_index('goTerm')
df2 = pd.read_csv('goTerms (1).csv')
df2['goTerm'] = df2['goTerm'].str.replace(' ', '')
temp = df2
df2 = df2.set_index('goTerm')

df3 = df1.join(df2).to_csv('final.csv')
temp.to_csv('goTerms.csv', mode='a', index=False)