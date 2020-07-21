
import numpy as np
import pandas as pd

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
suits = ['♥', '♦', '♠', '♣']

deck = {'Card':[], 'Suit':[]}


for suit in suits:
    for card in cards:
        deck['Card'].append(card)
        deck['Suit'].append(suit)

df = pd.DataFrame(deck)

num_observations = 10000

drawn_cards = {'Card':[], 'Suit':[]}
for obs in range(num_observations):
    drawn_cards['Card'].append(df.iloc[np.random.randint(len(df))]['Card'])
    drawn_cards['Suit'].append(df.iloc[np.random.randint(len(df))]['Suit'])

drawn_cards = pd.DataFrame(drawn_cards)

path = 'data/'

df.to_csv(path + 'deck.csv', index=False)
drawn_cards.to_csv(path + 'obs_full.csv', index=False)

len(drawn_cards)
