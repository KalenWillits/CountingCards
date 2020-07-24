# __Dependancies__
import numpy as np
np.random.seed(1111)
import pandas as pd
# Creating two lists of features to iterate over.
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦', '♠', '♣']
print(cards, suits)
deck = {'Card':[], 'Suit':[]}
# Assigning unique values to the deck
for suit in suits:
    for card in cards:
        deck['Card'].append(card)
        deck['Suit'].append(suit)
# Transforming from list, to dictionary, to Pandas DataFrame.
df = pd.DataFrame(deck)
# Writing the observations to "obs_full.csv".
cd_data = 'data/'
df.to_csv(cd_data+'deck.csv', index=False)
#Checking the contents of the deck
print(df.info())
