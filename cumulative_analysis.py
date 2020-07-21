import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
cd_data = 'data/'

plt.figure(figsize=(10,10))
df = pd.read_csv(cd_data+'cumulative_deck_obs.csv')

for i in range(len(xs)):
    plt.plot(xs[i], alpha=0.01, color='grey')

cumulative_mean = []
for i in range(len(xs[0])):
    cumulative_mean.append(xs[:,i].mean())

pd.DataFrame(cumulative_mean).describe()

plt.plot(cumulative_mean, color='red')
title = 'Mean of Cumulative Observation'
plt.title(title)
plt.grid()
plt.xticks([i for i in range(2, len(cumulative_mean), 2)])
plt.yticks([i for i in range(int(min(cumulative_mean)-1), int(max(cumulative_mean)+1), int(min(cumulative_mean)))])
plt.xlabel('Number of Cards Drawn')
plt.ylabel('Cumulative Card Value')
plt.savefig('figures/'+title+'.png')
