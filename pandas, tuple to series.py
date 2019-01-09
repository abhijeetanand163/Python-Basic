import pandas as pd
# converting tuple to Series
h = ('AA', '2012-02-01', 100, 10.2)
s = pd.Series(h)
print(type(s))
print(s)
