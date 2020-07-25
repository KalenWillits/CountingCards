# __Dependancies__
import numpy as np
np.random.seed(1111)
import pandas as pd
# Creating two lists of features to iterate over.
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
suits = ['♥', '♦', '♠', '♣']

deck = {'Card':[], 'Suit':[]}
# Assigning unique values to the deck
for suit in suits:
    for card in cards:
        deck['Card'].append(card)
        deck['Suit'].append(suit)
# Transforming from list, to dictionary, to Pandas DataFrame.
df = pd.DataFrame(deck)

cd_data = 'data/'
df.to_csv(cd_data+'deck_test.csv', index=False)
#Checking the contents of the deck
print(df.info())
