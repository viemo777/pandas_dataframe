import os


import numpy as np
import pandas as pd

arr = np.random.randint(1, 21, 10)

new_arr = np.arange(2, 12)
print(arr)
print(new_arr)
print(arr + new_arr)



arr = np.random.randint(0, 10, 7)

new_arr = arr * 3
print(arr)
print(new_arr)

arr = np.sqrt(np.arange(7, 28))
print(arr)

df = pd.DataFrame(np.random.randn(4, 3), ['a', 's', 'd', 'f'], ['X', 'Y', 'Z'])
print(df)

print(df > 0)

print(df[df > 0])
print(df[(df['Z'] > 0) & (df['X'] > 0)])
print(df[(df['Z'] > 0) & (df['X'] < 0)])

print(df.reset_index())

new_list = [100, 101, 102, 103]
df['inCol'] = new_list
print(df)
df.set_index('inCol', inplace=True)
print(df)

col = ['A', 'B', 'C', 'D']
strs = [10, 20, 30, 40, 50]
my_df = pd.DataFrame(np.random.randint(1, 101, 20).reshape(5, 4), strs, col)

print(my_df)
print(my_df[my_df['A'] < 30])

print(my_df[(my_df['A'] < 50) & (my_df['B'] < 40)])

print(my_df[(my_df['C'] > 20) & (my_df['D'] < 70)][['A', 'B']])

print('\n------------ next example------------\n')
mult_ind = pd.MultiIndex(levels=[['A', 'B', 'C'], ['left', 'right']],
                         codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])
df = pd.DataFrame(np.random.randn(6, 3), mult_ind, ['X', 'Y', 'Z'])
print(mult_ind)
print(df)
print(df.loc['C'].loc['left']['X'])
df.index.names = ['Points', 'Sides']
print(df.xs('right', level = 'Sides'))

print('------------ os example------------')

print(os.getcwd())
print(os.listdir())



print('------------ csv example------------')

my_csv = pd.read_csv('us-500.csv')
my_df = my_csv['web'].head(10)
my_df.to_csv('my_csv.csv', index = False)

print('------------ excel  example------------')

my_pd = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders')
my_xls = my_pd[['OrderDate', 'Total']].to_excel('my_xls.xlsx', sheet_name='Main')

print('------------ html example------------')

my_pd = pd.read_html('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
print(my_pd[11].head(5))

print('------------ json example------------')

my_pd_json = my_pd[11].head(5).to_json()
print(my_pd_json)