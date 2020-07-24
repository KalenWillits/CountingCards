import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
cd_data = 'data/'

plt.figure(figsize=(10,10))
df = pd.read_csv(cd_data+'cumulative_deck_obs.csv')

df = df.transpose()

plt.plot(df, alpha)
