import pandas as pd
import csv

csv = pd.read_csv('./file.csv', index_col=0, header=[0,1,2])
csv.to_hdf('./file.h5','df_with_missing',format='table', mode='w')
h5_test = pd.read_hdf('./file.h5')
print(csv.equals(h5_test))