import pandas as pd

vgs = pd.read_csv('vgsales.csv')
print(vgs)

print(vgs.head(10))

print(vgs.info())


print(vgs['EU_Sales'].mean())

print(vgs['JP_Sales'].max())


print(vgs.loc[vgs['Name'] == 'Brain Age 2: More Training in Minutes a Day']['Genre'])


print(vgs.loc[vgs['Name'] == 'Grand Theft Auto: Vice City']['Global_Sales'])


ss = vgs['Global_Sales'].min()
print(vgs.loc[vgs['Global_Sales'] == ss]['Name'])
