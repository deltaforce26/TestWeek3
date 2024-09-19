import requests as re
import services.player_service as ps
from models.player import Player


def get_players(season: str):
    try:
        data = re.get(f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}').json()
        for item in data:
            print(item)
            ps.create_player(item)
    except Exception as e:
        print(e)
        exit()



def get_stats(season: str):
    try:
        data = re.get(f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}').json()
        for item in data:

    except Exception as e:
        print(e)
        exit()