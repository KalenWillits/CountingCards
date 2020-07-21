import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
cd_data = 'data/'

df = pd.read_csv(cd_data+'cumulative_deck_obs.csv')
