
import pandas as pd
import numpy as np
df=pd.read_csv('Iris.csv')
df.head()
df.drop(columns='Id',inplace=True)
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
print(x_train.shape)
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(
n_estimators=15,max_depth=10)
rfc.fit(x_train,y_train)
import joblib
joblib.dump(rfc,'model/rfc.pkl') 
print('something something')

   