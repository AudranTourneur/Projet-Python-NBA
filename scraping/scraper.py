import time

import requests

PLAYERS_URL = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2022-23&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
TEAMS_URL = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2022-23&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="


def scrap_url_into_file(url, filename):
    headers_text = """
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: fr-FR,fr;q=0.9
Connection: keep-alive
Host: stats.nba.com
Origin: https://www.nba.com
Referer: https://www.nba.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Sec-GPC: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
sec-ch-ua: "Chromium";v="118", "Brave";v="118", "Not=A?Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux" 
"""

    headers = {}
    for line in headers_text.splitlines():
        if line:
            key, value = line.split(": ", 1)
            headers[key] = value

    # get response, abort after 10s
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        # print("Response:", response.text)
        json_data = response.json()
        # print(json_data)

        # write into data/teams.json
        with open(filename, "w") as f:
            f.write(response.text)
            print("Successfully wrote into " + filename + ' (' + str(len(response.text)) + ' bytes)')
    else:
        print("Error: " + str(response.status_code))


import time

if __name__ == '__main__':
    # scrap_url_into_file(PLAYERS_URL, "../data/players.json")
    # scrap_url_into_file(TEAMS_URL, "../data/teams.json")

    for i in range(2000, 2023):
        years = str(i) + '-' + str(i + 1)[2:]

        url_to_scrap = ("https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division"
                        "=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base"
                        "&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0"
                        "&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season="
                        + years +
                        "&SeasonSegment=&SeasonType"
                        "=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=")

        print(years, '=>', url_to_scrap)

        scrap_url_into_file(url_to_scrap, "../data/teams_" + years + ".json")

        time.sleep(1)
