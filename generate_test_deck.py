import numpy as np
np.random.seed(1111)
import pandas as pd
cd_data = 'data/'
df = pd.read_csv(cd_data+'obs_full_numeric'+'.csv')
df = df[['Card Value']]
# split the deck ( Must be a int between 0 and 51)

arr = np.array(df)
arr = arr.tolist()
new_arr = []
for p in arr:
    new_arr.append(p[0])

split_deck = []
for i in range(len(arr)):
    drawn_card = new_arr.pop(np.random.randint(len(new_arr)))
    split_deck.append(drawn_card)
test_deck = np.cumsum(split_deck)
test_deck = pd.DataFrame({'Card Value': test_deck})
test_deck.to_csv(cd_data+'test_deck.csv', index=False)
