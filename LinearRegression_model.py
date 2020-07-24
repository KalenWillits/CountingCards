import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score
import numpy as np
import pandas as pd
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
cd_data = 'data/'

df = pd.read_csv(cd_data+'cumulative_deck_obs.csv')
# Where I split the X and y is where the the probability is deterimined
X = np.array(df.columns).reshape(-1,1) # The x axis is the card drawn count
y = df.transpose() # The y value is the cumulative sum.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1111)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred = pd.DataFrame(y_pred)
scores = cross_val_score(model, X, y, cv=5)
print('Cross Validation: {}%'.format(np.mean(scores)*100))
# __Test Data__
with open('drawn_card.txt', 'r') as file:
    drawn_card = int(file.read())



test_pred = model.predict(np.array(drawn_card).reshape(-1,1))
print('Prediction \nMean: ', np.mean(test_pred), '\nRange: [',
 np.min(test_pred), ',', np.max(test_pred), ']')
#plt.plot(test_pred)
