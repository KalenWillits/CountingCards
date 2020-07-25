
import numpy as np
import pandas as pd

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
suits = ['♥', '♦', '♠', '♣']

for suit in suits:
    for card in cards:
        pre_deck.append([card,suit])


for i in num_cards_to_remove:
    pre_deck.pop(np.random.randint(len(pre_deck)))

num_observations = 10000

drawn_cards = {
'Card': [],
'Suit': []
}
for obs in range(num_observations):
    drawn_card = pre_deck[np.random.randint(len(pre_deck))]
    drawn_cards['Card'].append(drawn_card[0])
    drawn_cards['Suit'].append(drawn_card[1])

drawn_cards = pd.DataFrame(drawn_cards)
drawn_cards['Card'].unique()
path = 'data/'
drawn_cards.to_csv(path + 'obs_missing.csv', index=False)
