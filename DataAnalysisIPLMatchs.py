import numpy as np # numerical computing
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 8)

matches = pd.read_csv('matches.csv')
matches.shape
matches.head()
matches.describe()
matches.info()
matches['id'].max()

#no of seasons of IPL
matches['season'].unique()

len(matches['season'].unique())

#team won by maximum runs
matches.iloc[matches['win_by_runs'].idxmax()]

#team won by maximum wickets
matches.iloc[matches['win_by_wickets'].idxmax()]

#win with close margin
matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmax()]

matches[matches[matches['win_by_runs'].ge(1)].win_by_runs.min() == matches['win_by_runs']]['winner']

#team won with minimum wickets
matches.iloc[matches[matches['win_by_wickets'].ge(1)].win_by_wickets.idxmax()]

#season with most no of matches
sns.countplot(x='season', data=matches)
plt.show()

#sucessful team
data = matches.winner.value_counts()
sns.barplot(y=data.index, x=data, orient='h')
#top player
top_players = matches.player_of_match.value_counts()[:10]

fig, ax=plt.subplots()
ax.set_ylim([10,20])
ax.set_ylabel("Count")
ax.set_title("Top player of the match winners")

#top_players.plot.bar()

sns.barplot(x=top_players.index, y=top_players, orient='v'); 
plt.show()

#toss winning match winning
ss=matches['toss_winner']==matches['winner']

ss.groupby(ss).size()

round(ss.groupby(ss).size/ss.count()* 100,2)

sns.countplot(ss)

matches[matches['win_by_runs']>0].groupby(['winner'])['win_by_runs'].apply(np.median).sort_values(ascending=False)

fig, ax=plt.subplots()

ax.set_title("Winning by Runs - Team Performance")
sns.boxplot(y='winner', x='win_by_runs', data=matches[matches['win_by_runs']>0],orient='h')
plt.show()

matches[matches['win_by_wickets']>0].groupby(['winner'])['win_by_wickets'].apply(np.median).sort_values(ascending=False)

fig, ax=plt.subplots()
ax.set_title("Winning by Wickets - Team Performance")
sns.boxplot(y='winner', x='win_by_wickets', data=matches[matches['win_by_wickets']>0],orient='h')
plt.show()




