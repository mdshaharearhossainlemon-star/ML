import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn import metrics

df = pd.read_csv('/content/salary_data (1).csv')
features = df.iloc[:, :-1].values
target = df.iloc[:, 1].values

X_train, X_test, Y_train, Y_test = train_test_split(features, target, test_size = 0.33, random_state = 2)
model =  Lasso(alpha=1.0)
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
result = pd.DataFrame({'actual' : Y_test, 'Predicted salary' : predictions})

print(result)
print("R² Score:", metrics.r2_score(Y_test, predictions))
print("Mean Absolute Error:", metrics.mean_absolute_error(Y_test, predictions))
