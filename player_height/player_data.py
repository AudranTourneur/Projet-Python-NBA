import json

import pandas as pd


def create_players_dataset():
    # Read in the stats.json file
    stats = pd.read_json('/stats.json')
    # Rename the columns
    stats.columns = ['PLAYER_ID', 'HEIGHT', 'POSITION']

    # Read in the players.json file
    with open('../data/players.json', 'r') as f:
        json_data = json.load(f)

    # Extract the relevant information from the JSON structure
    columns = json_data['resultSets'][0]['headers']
    data = json_data['resultSets'][0]['rowSet']

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Convert relevant columns to numeric
    df['W'] = pd.to_numeric(df['W'])
    df['L'] = pd.to_numeric(df['L'])
    df['PTS'] = pd.to_numeric(df['PTS'])

    # Calculate Win Rate and Average Points per Game
    df['WinRate'] = df['W'] / (df['W'] + df['L'])
    df['AvgPointsPerGame'] = df['PTS'] / df['GP']

    # Merge the DataFrames on PLAYER_ID
    merged = pd.merge(stats, df, on='PLAYER_ID')

    # Keep only PLAYER_ID, HEIGHT, POSITION, WinRate, AvgPointsPerGame
    merged = merged[['PLAYER_ID', 'HEIGHT', 'POSITION', 'WinRate', 'AvgPointsPerGame']]
    print(merged)

    return merged