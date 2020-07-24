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
# Defining the number of cards to draw from our deck
num_observations = 10000
# Drawing the cards as observations(obs) and turning the dictionary into a DataFrame.
drawn_cards = {'Card':[], 'Suit':[]}
for obs in range(num_observations):
    drawn_cards['Card'].append(df.iloc[np.random.randint(len(df))]['Card'])
    drawn_cards['Suit'].append(df.iloc[np.random.randint(len(df))]['Suit'])
drawn_cards = pd.DataFrame(drawn_cards)
# Writing the observations to "obs_full.csv".
cd_data = 'data/'
df.to_csv(cd_data+'deck.csv', index=False)
drawn_cards.to_csv(cd_data+'obs_full.csv', index=False)
#Checking the contents of the deck
print(df.info())
