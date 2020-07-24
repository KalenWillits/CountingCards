import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cd_data = 'data/'
cd_figures = 'figures/'

df = pd.read_csv(cd_data+'obs_full_numeric.csv')
plt.figure(figsize=(10,10))
fig, axs = plt.subplots(2,2)

bins = 13

axs[0, 0].hist(df[df['Suit'] == 0.01]['Card'], color='black', label='♠', bins=bins)
axs[1, 0].hist(df[df['Suit'] == 0.0001]['Card'], color='red', label='♥', bins=bins)
axs[0, 1].hist(df[df['Suit'] == 0.000001]['Card'], color='pink', label='♦', bins=bins)
axs[1, 1].hist(df[df['Suit'] == 0.00000001]['Card'], color='grey', label='♣', bins=bins)

title = 'Card Distrobutions by Suit'
fig.suptitle(title)
fig.legend()
axs[0,0].set(ylabel='Card Counts')
axs[1,0].set(xlabel='Card Value', ylabel='Card Counts')
axs[1,1].set(xlabel='Card Value')
plt.show()
plt.savefig(cd_figures+title+'.png')
