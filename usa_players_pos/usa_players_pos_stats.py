import pandas as pd
import matplotlib.pyplot as plt
import json

df_country = pd.read_json('../analysis/country_stats.json')
df_country.columns = ['PLAYER_ID', 'COUNTRY']

df_pos = pd.read_json('../analysis/pos_stats.json')
df_pos.columns = ['PLAYER_ID', 'HEIGHT', 'POS']

df = pd.merge(df_country, df_pos, on='PLAYER_ID')

df_usa = df[df['COUNTRY'] == 'USA']

# Plot pie chart with each position
df_usa['POS'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, legend=False, fontsize=8)
plt.title('USA Players Positions', fontsize=20)
plt.ylabel('')
plt.show()
