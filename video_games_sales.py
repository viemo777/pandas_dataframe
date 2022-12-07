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

print('11. What is the average value of sales of all video games per genre in Japan?')
print(vgs.groupby(['Genre'])['JP_Sales'].mean())

print('12. How many unique names of video games in this dataframe?')
print(vgs['Name'].nunique())

print('13. Get the 3 most common genres of video games worldwide')
print(vgs.groupby(['Genre'])['Global_Sales'].count().sort_values().head(3))

print('14. How many video games have "super" word in their names?')
my_np = vgs['Name'].unique()
count = 0
for x in my_np:
    if 'super' in str(x.lower().split()):
        count += 1
print(count)
