import pandas as pd
data =pd.read_csv('HousingData.csv')
data

data.head(2)
data.info()
data.describe()

data.corr()

from seaborn import scatterplot

x =data['RM']
y =data['MEDV']
scatterplot(x=x,y=y)

from sklearn.model_selection import train_test_split
xtest,ytest,xtrain,ytrain = train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
lm =LinearRegression()
model = lm.fit(xtrain,ytrain)

b1= model.coef_
b0= model.intercept_
b0
b1

from seaborn import regplot

x =data['RM']
y =data['MEDV']
regplot(x=x,y=y)

pred =model.prediction(xtest)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(ytest,pred)

from sklearn.metrics import mean_squared_error
mean_squared_error(ytest,pred)

print(ytest)
print(pred)
