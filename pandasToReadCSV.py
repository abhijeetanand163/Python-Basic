import pandas as pd
# This method is to read CSV files from Local environment.
file_path = 'E:\Sample data\FL_insurance_sample.csv'
#• index_col = None : there is no index i.e. first column is data
casts = pd.read_csv(file_path, index_col=None)
# .head() function prints first five rows.
print(casts.head())
# .tail() function prints last five rows.
print(casts.tail())
