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

with open('../data/players_country.json', 'w') as file:
    # Ad [
    file.write('[\n')
    # Get player ID and Height
    for player in players_data:
        player_id = player['PERSON_ID']
        player_country = player['COUNTRY']
        object = {
            'player_id': player_id,
            'player_country': player_country,
        }

        # Add , if not last object
        if player != players_data[-1]:
            file.write(json.dumps(object) + ',\n')

        # Add \n if last object
        else:
            file.write(json.dumps(object) + '\n')

    # Add ]
    file.write(']')
