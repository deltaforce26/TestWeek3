import requests as re



def get_players(season: str):
    try:
        data = re.get(f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}').json()

    except Exception as e:
        print(e)
        exit()