import pandas as pd
import matplotlib.pyplot as plt

# Read in the stats.json file
df = pd.read_json('../stats.json')

# Rename the columns
df.columns = ['PLAYER_ID', 'HEIGHT', 'POSITION']

# Create a subplot with an histogram for each position (G, F, C, G-F, F-G, F-C, C-F)
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Add some space between the plots
fig.subplots_adjust(hspace=0.5)

# Plot the histograms with 10 bins
axs[0, 0].hist(df[df['POSITION'] == 'G']['HEIGHT'], bins=10)
axs[0, 0].set_title('Guards')
axs[0, 0].set_xlabel('Height (cm)')
axs[0, 0].set_ylabel('Number of Players')
axs[0, 0].set_xlim(175, 230)
axs[0, 0].set_ylim(0, 80)
axs[0, 1].hist(df[df['POSITION'] == 'F']['HEIGHT'], bins=10)
axs[0, 1].set_title('Forwards')
axs[0, 1].set_xlabel('Height (cm)')
axs[0, 1].set_ylabel('Number of Players')
axs[0, 1].set_xlim(175, 230)
axs[0, 1].set_ylim(0, 80)
axs[1, 0].hist(df[df['POSITION'] == 'C']['HEIGHT'], bins=10)
axs[1, 0].set_title('Centers')
axs[1, 0].set_xlabel('Height (cm)')
axs[1, 0].set_ylabel('Number of Players')
axs[1, 0].set_xlim(175, 230)
axs[1, 0].set_ylim(0, 80)
axs[1, 1].hist(df[df['POSITION'] == 'G-F']['HEIGHT'], bins=10)
axs[1, 1].set_title('Guards-Forwards')
axs[1, 1].set_xlabel('Height (cm)')
axs[1, 1].set_ylabel('Number of Players')
axs[1, 1].set_xlim(175, 230)
axs[1, 1].set_ylim(0, 80)
axs[2, 0].hist(df[df['POSITION'] == 'F-G']['HEIGHT'], bins=10)
axs[2, 0].set_title('Forwards-Guards')
axs[2, 0].set_xlabel('Height (cm)')
axs[2, 0].set_ylabel('Number of Players')
axs[2, 0].set_xlim(175, 230)
axs[2, 0].set_ylim(0, 80)
axs[2, 1].hist(df[df['POSITION'] == 'F-C']['HEIGHT'], bins=10)
axs[2, 1].set_title('Forwards-Centers')
axs[2, 1].set_xlabel('Height (cm)')
axs[2, 1].set_ylabel('Number of Players')
axs[2, 1].set_xlim(175, 230)
axs[2, 1].set_ylim(0, 80)

# For each subplot, add a vertical line for the mean height by position
axs[0, 0].axvline(x=df[df['POSITION'] == 'G']['HEIGHT'].mean(), color='red')
axs[0, 1].axvline(x=df[df['POSITION'] == 'F']['HEIGHT'].mean(), color='red')
axs[1, 0].axvline(x=df[df['POSITION'] == 'C']['HEIGHT'].mean(), color='red')
axs[1, 1].axvline(x=df[df['POSITION'] == 'G-F']['HEIGHT'].mean(), color='red')
axs[2, 0].axvline(x=df[df['POSITION'] == 'F-G']['HEIGHT'].mean(), color='red')
axs[2, 1].axvline(x=df[df['POSITION'] == 'F-C']['HEIGHT'].mean(), color='red')

# Show the plot
plt.show()
