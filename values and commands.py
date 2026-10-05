import pandas as pd
df = pd.read_csv('studentperformance.csv')
print(df.values)
print('\n')
print(df.major)
print('\n')
print(df.major[0])
print('\n')
print(df.loc[0])