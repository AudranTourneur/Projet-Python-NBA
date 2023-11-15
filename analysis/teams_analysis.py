import pandas as pd
import json

from pandas import DataFrame


def build_season_dataframe(year: int) -> DataFrame:
    years = str(year) + '-' + str(year + 1)[2:]
    file_name = '../data/teams_' + years + '.json'
    json_data = open(file_name).read()
    data = json.loads(json_data)

    headers = data['resultSets'][0]['headers']
    actual_data = data['resultSets'][0]['rowSet']

    df = pd.DataFrame(actual_data, columns=headers)

    df = df.sort_values(by=['W'], ascending=False)

    # Let's add a column with the rank of the team (1st, 2nd, 3rd, etc. based on the number of wins)
    df['RANK'] = df['W'].rank(ascending=False)

    final_season_view = df[['TEAM_NAME', 'W', 'RANK']]
    print(final_season_view)

    return final_season_view


def get_eligible_teams() -> [str]:
    eligible_teams: [str] = []

    first_year = 2000
    last_year = 2022

    for year in [first_year, last_year]:
        df = build_season_dataframe(year)
        # let's get the first 5 teams

        for index, row in df.head(5).iterrows():
            team_name = row['TEAM_NAME']
            eligible_teams.append(team_name)

    return eligible_teams


def run():
    final_df = pd.DataFrame()
    # This df is a timeseries of the rank of each team for each season
    # This object will hold as columns the name of the team
    # As rows, the rank of the team for each season
    # The index will be the season (2000, 2001, 2002, etc.)

    eligible_teams = get_eligible_teams()

    for i in range(2000, 2023):

        # let's add the rank of the team for this season to the final_df
        # we will use the team name as column name
        # we will use the season as index

        final_season_view = build_season_dataframe(i)

        for index, row in final_season_view.iterrows():
            team_name = row['TEAM_NAME']
            if team_name not in eligible_teams:
                continue
            rank = row['RANK']
            final_df.at[i, team_name] = rank

    print(final_df)

    # Let's plot this timeseries, rank is upside down
    # plot into timeseries.png
    fig = final_df.plot(figsize=(10, 5), title='Rank of teams over time')
    # the previous figure should have the y axis inverted, change it:
    fig.invert_yaxis()
    fig.get_figure().savefig('timeseries.png')



def get_all_teams_available() -> [str]:
    all_teams: [str] = []

    first_year = 2000
    last_year = 2022

    for year in [first_year, last_year]:
        df = build_season_dataframe(year)
        # let's get all teams this year

        for index, row in df.iterrows():
            team_name = row['TEAM_NAME']
            all_teams.append(team_name)

    all_teams = list(dict.fromkeys(all_teams))

    return all_teams

def resolve_team_from_user_input(all_teams: [str]) -> str:
    team_to_track = input("Please enter a team you wish to track:")
    while team_to_track not in all_teams:
        print("The team you entered is not available, please try again")
        team_to_track = input("Please enter a team you wish to track:")

    return team_to_track

def interactive_team_tracking():
    all_teams = get_all_teams_available()
    print("The following teams are available:")
    print("\n".join(all_teams))
    team_to_track = resolve_team_from_user_input(all_teams)






if __name__ == '__main__':
    interactive_team_tracking()
