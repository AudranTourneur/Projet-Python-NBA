import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

from player_data import create_players_dataset

if __name__ == '__main__':
    json_data = open('../data/players_2022-23.json').read()
    data = json.loads(json_data)

    headers = data['resultSets'][0]['headers']
    actual_data = data['resultSets'][0]['rowSet']

    df = create_players_dataset()

    print('print all columns')
    print(df.columns)

    def joinplot():
        plt.clf()
        sns.jointplot(x='W', y='PF', data=df)
        plt.savefig('pf_wins.png')

    print('uwu ?')

    reduced_df = df[["WinRate", "FGM", "AST", "REB", "FGA", "PF", "POSITION"]]

    dataset = create_players_dataset()


    def giga_graph():
        plt.clf()
        sns.pairplot(data=reduced_df, hue="POSITION")
        plt.savefig('lots_of_correlations.png')


    giga_graph()
    print('end')
