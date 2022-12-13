import pandas as pd
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import scipy


#Reads in the data 
df = pd.read_csv('data/twitter_df_w_sentiment.csv')

df = df.drop(columns=['Unnamed: 0.1'])
df = df.drop(columns=['Unnamed: 0'])
df = df.drop(columns=['edit_history_tweet_ids'])


df= df[df.retweeted.notnull()]

df = df[df.location.notnull()]

df.to_csv('data/twitter_graph_location.csv')

print('done')