import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
cd_data = 'data/'

x = pd.read_csv(cd_data+'obs_train.csv')
y = pd.read_csv(cd_data+'obs_test.csv')

dx = pd.get_dummies(x)
dy = pd.get_dummies(y)

x_train, x_test, y_train, y_test = train_test_split(dx, dy, test_size=0.25, random_state=1111)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

plt.plot(y_pred)
