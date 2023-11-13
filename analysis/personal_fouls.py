import pandas as pd
import json
import seaborn as sns
from pandas import DataFrame
import matplotlib.pyplot as plt


if __name__ == '__main__':
    json_data = open('../data/players_2022-23.json').read()
    data = json.loads(json_data)

    headers = data['resultSets'][0]['headers']
    actual_data = data['resultSets'][0]['rowSet']

    df = pd.DataFrame(actual_data, columns=headers)

    print('print all columns')
    print(df.columns)

    def joinplot():
        plt.clf()
        sns.jointplot(x='W', y='PF', data=df)
        plt.savefig('pf_wins.png')

    print('uwu ?')

    #reduced_df = df[['W', 'PF', 'FG3M', 'FG3A']]
    reduced_df = df[["FGM", "AST", "REB", "FGA"]]


    def giga_graph():
        plt.clf()
        sns.pairplot(data=reduced_df)
        plt.savefig('giga_graph.png')

    giga_graph()
    print('end')
