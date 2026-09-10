import pandas as pd
df=pd.read_csv('House Price Prediction Dataset.csv')
df.shape
df.info()
df.duplicated()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Location']=le.fit_transform(df['Location'])
df['Condition']=le.fit_transform(df['Condition'])
df['Garage']=le.fit_transform(df['Garage'])
df['Condition']
corr=df.corr()
print(corr)
x=df[['Area','Bedrooms','Bathrooms','Floors','YearBuilt','Location','Condition','Garage']]
y=df['Price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x_test)
print(x_train)
print(y_test)
print(y_train)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error,root_mean_squared_error
rscore=r2_score(y_test,y_pred)
print(rscore)
mae=mean_absolute_error(y_test,y_pred)
print(mae)
mse=mean_squared_error(y_test,y_pred)
print(mse)
rmse=root_mean_squared_error(y_test,y_pred)
print(rmse)
df['Area'].corr(df['Price'])
df['Bedrooms'].corr(df['Price'])
df['Bathrooms'].corr(df['Price'])
df['Floors'].corr(df['Price'])
df['YearBuilt'].corr(df['Price'])
df['Location'].corr(df['Price'])
df['Condition'].corr(df['Price'])
df.corr(numeric_only=True)
import matplotlib.pyplot as plt
plt.scatter(df['Area'],df['Price'])
