import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
cd_data = 'data/'

df = pd.read_csv(cd_data+'cumulative_deck_obs.csv')
df = df.transpose()
# Where I split the X and y is where the the probability is deterimined
split = 0.6
df.shape
X = df.loc[:,:str(int(df.shape[1]*split))]
y = df.loc[:,str(int(df.shape[1]*split)+1):]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=1111)

model = SVC()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred = pd.DataFrame(y_pred)
scores = cross_val_score(model, X, y, cv=5)
print('Accuracy: {}%'.format(np.mean(scores)))
