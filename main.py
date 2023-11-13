import requests


def scrap_nba_teams():
    # TARGET_URL = "https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2004-05&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="
    TARGET_URL = "htps://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2023-24&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="

    # SET COOKIE HEADERS
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

    print(headers)

    # get response, abort after 10s
    response = requests.get(TARGET_URL, headers=headers, timeout=10)

    if response.status_code == 200:
        print("Response:", response.text)
        json_data = response.json()
        print(json_data)

        # write into data/teams.json
        with open("data/teams.json", "w") as f:
            f.write(response.text)

        print(" === OK")

    else:
        print("Error: " + str(response.status_code))


if __name__ == '__main__':
    scrap_nba_teams()
    print("aaaaaaaaaaaaaaaaaaa")
