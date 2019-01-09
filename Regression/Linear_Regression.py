import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(18,10))
x = np.array([[1,2,3,4,5,6,7,8,9]]).T
y= np.array([[19,20,20.5,21.5,22,23,23,25.5,24]]).T
plt.scatter(x,y, color ='blue')
plt.show()

# Linear Regression on data set
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(x,y)
print ('Coefficient:', regr.coef_)
print ('Intercept:', regr.intercept_)


# plotting the best fit line over the data

plt.scatter(x, y, color ="blue")
plt.plot(x, regr.coef_[0][0]*x + regr.intercept_[0], color = 'red')
plt.plot(x, regr.coef_*x + regr.intercept_, color = 'blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

