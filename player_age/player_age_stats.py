import pandas as pd
import matplotlib.pyplot as plt
import json

# Read in the data

json_data = open('../data/players.json').read()
data = json.loads(json_data)

headers = data['resultSets'][0]['headers']
actual_data = data['resultSets'][0]['rowSet']

df = pd.DataFrame(actual_data, columns=headers)
df = df[["AGE", "PTS", "GP"]]

# Calculate the average point per game PTS / GP
df["PPG"] = df["PTS"] / df["GP"]

# Make age into an int
df["AGE"] = df["AGE"].astype(int)

# Create a boxplot with PPG and AGE:
df.boxplot(column="PPG", by="AGE")
plt.title("Average Points Per Game by Age")
plt.suptitle("")
plt.xlabel("Age")
plt.ylabel("Points Per Game")
plt.show()
    
