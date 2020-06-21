# %% codecell

import numpy as np
import pandas as pd

# generating a dataset that creates a deck of cards with one card missing.
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
suits = ['♥', '♦', '♠', '♣']

deck = []

for suit in suits:
    for card in cards:
        deck.append(card+suit)

#Checking deck for correct values
print(deck)
print(len(deck))
deck[0:5]
# %% codecell
#removing a random card from the deck
np.random.seed(42)
deck.pop(np.random.randint(len(deck)))

#verifying there are 51 cards in the deck.
print(len(deck))

# %% codecell
#Generating a dataset of observations to draw 5 cards. Where the index is the observation number and the column "Hand" is the 5 cards drawn.
observations = {'Hand':[]}
n_observations = 10000
for hand in range(n_observations):
    np.random.shuffle(deck)
    observations['Hand'].append(deck[0:5])
df = pd.DataFrame(observations)
# %% codecell
df.head()

# %% codecell
!pwd
# Writing the new observations dataframe to a .csv file.
path = 'deck_of_cards/data/'
df.to_csv(path + 'observations.csv')
