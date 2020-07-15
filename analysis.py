
#__import modules__
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#__Variable library__
cd_data = 'data/'
data = 'obs_train.csv'
df = pd.read_csv(cd_data + data)
cards = df['Card']
suits = df['Suit']
#__Data visualization__
cd_figures = 'figures/'
title = 'Observed Cards'
plt.figure(figsize=(10,10))
plt.scatter(x=cards, y=suits, s=300)
plt.title(title)
plt.xlabel('Card')
plt.ylabel('Suit')
plt.grid()
plt.savefig(cd_figures+title+'.png')
