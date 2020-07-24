import numpy as np
np.random.seed(1111)
import pandas as pd
cd_data = 'data/'
df = pd.read_csv(cd_data+'deck.csv')
# Ranking suits by clubs, diamonds, hearts, spades from lowest to highest.
df['Suit'].unique()
cards_to_replace = {'A':14, 'J':11, 'K':13, 'Q':12}
suits_to_replace = {'♦':0.000001, '♥':0.0001, '♠':0.01, '♣':0.00000001}
df['Card'].replace(to_replace=cards_to_replace, inplace=True)
df['Suit'].replace(to_replace=suits_to_replace, inplace=True)

# Changing the values from objects to floats
df['Card'] = pd.to_numeric(df['Card']).astype(float)
card_value = df['Card'] + df['Suit']
df['Card Value'] = card_value
# Sorting the numeric deck.
df = df.apply(sorted)
# Creating the random walk using a cumulative sum function.
cs = np.cumsum(df['Card Value'])
df['Cumulative'] = cs
# Generatin training and testing data.
df['Card Value']
cumulative_deck_obs = {}
num_observations = 10000
for idx in list(range(num_observations)):

    deck = np.array(df['Card Value'])
    np.random.shuffle(deck)
    np.cumsum(deck)
    cumulative_deck_obs[idx] = np.cumsum(deck)
cumulative_deck_obs = pd.DataFrame(cumulative_deck_obs).transpose()
df.to_csv(cd_data+'obs_full_numeric.csv', index=False)

# writing to the .csv file.
cumulative_deck_obs.to_csv(cd_data+'cumulative_deck_obs.csv', index=False)
# checing the results
print(cumulative_deck_obs.describe())
