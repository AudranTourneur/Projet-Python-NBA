import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.nba.com/players'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Get <script id="__NEXT_DATA__" type="application/json">
script = soup.find('script', id='__NEXT_DATA__')

# Get players data
players_data = json.loads(script.contents[0])['props']['pageProps']['players']


def foot_to_centimeter(foot):
    foot = foot.split('-')
    foot = int(foot[0]) * 30.48 + int(foot[1]) * 2.54
    return round(foot, 2)


with open('../data/players_height_position.json', 'w') as file:
    # Ad [
    file.write('[\n')
    # Get player ID and Height
    for player in players_data:
        player_id = player['PERSON_ID']
        player_height = player['HEIGHT']
        centimeter_height = foot_to_centimeter(player_height)
        player_pos = player['POSITION']
        object = {
            'player_id': player_id,
            'player_height': centimeter_height,
            'player_pos': player_pos
        }

        # Add , if not last object
        if player != players_data[-1]:
            file.write(json.dumps(object) + ',\n')

        # Add \n if last object
        else:
            file.write(json.dumps(object) + '\n')

    # Add ]
    file.write(']')
