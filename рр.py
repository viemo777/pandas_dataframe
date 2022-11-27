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

