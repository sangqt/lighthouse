import pandas as pd

df = pd.read_csv('milk_32.csv')
df = df.drop(columns = ['Unnamed: 0'])
df['Total Milk Production'] = df['Number of Cows'] * df['Monthly milk production: pounds per cow']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']
df['Year'] = df['Month'].str.slice(0, 2)
df.groupby(['Year']).sum()
