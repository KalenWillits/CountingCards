# __Dependancies__
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
cd_data = 'data/'
# __Load Data__
plt.figure(figsize=(10,10))
df = pd.read_csv(cd_data+'cumulative_deck_obs.csv')
# Changing to a numpy array (xs) to be iterated over and placed on the plot.
xs = np.array(df)
for i in range(len(xs)):
    plt.plot(xs[i], alpha=0.002, color='grey')
# Calculating the mean for each array and plotting that in red.
cumulative_mean = []
for i in range(len(xs[0])):
    cumulative_mean.append(xs[:,i].mean())
# Changing the mean back to a DataFrame.
pd.DataFrame(cumulative_mean).describe()

# Generating the plot and saving it.
plt.plot(cumulative_mean, color='red')
title = 'Mean of Cumulative Observation'
plt.title(title)
plt.grid()
plt.xticks([i for i in range(2, len(cumulative_mean), 2)])
plt.yticks([i for i in range(int(min(cumulative_mean)-1), int(max(cumulative_mean)+1), int(min(cumulative_mean)))])
plt.xlabel('Number of Cards Drawn')
plt.ylabel('Cumulative Card Value')
plt.savefig('figures/'+title+'.png')
