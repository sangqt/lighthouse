df = pd.read_csv('milk.csv', sep=r'\s*,\s*',header=0, encoding='ascii', engine='python')
max_milk = df['Month'][df['Monthly milk production: pounds per cow'].idxmax()]
print(f'The month and year with most milk is {max_milk}')
least_milk = df['Month'][df['Monthly milk production: pounds per cow'].idxmin()]
print(f'The month and year with least milk is {least_milk}')
df['year'] = df['Month'].str.slice(0, 2)
max_produce = 0
max_year = ''
for yr in df['year'].unique():
    tmp = sum(df.loc[df['year'] == yr]['Monthly milk production: pounds per cow'])
    if tmp > max_produce:
        max_year = yr
        max_produce = tmp

print(f'Milk is produced most in 20{max_year} and produced {max_produce} liters')
