import pandas as pd
# This method is to read CSV files from Local environment.
file_path = 'E:/sample data/release_dates.csv'
df = pd.read_csv(file_path, index_col=None)
# finding unique elements in "country" column
print(df['year'].unique())
#Creating a new dataframe df1 which takes input from df with year >= 2000
df1=df[df['year']>=2000]
#Saving df1 into a new CSV file at following location with this file name
df1.to_csv('E:/sample data/release_dates_after_2000.csv')
