import pandas as pd
# using dataframe of pandas
data = { 'name' : ['AA', 'IBM', 'GOOG'],
'date' : ['2001-12-01', '2012-02-10', '2010-04-09'],
'shares' : [100, 30, 90],
'price' : [12.3, 10.3, 32.2] }
df = pd.DataFrame(data)
print(type(df))
print(df)
df["owner"]= "unknown"
print(df)