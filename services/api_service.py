import requests as re
from services.stats_service import create_stat


# def get_players(season: str):
#     try:
#         data = re.get(f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}').json()
#         for item in data:
#             print(item)
#
#     except Exception as e:
#         print(e)
#         exit()



def get_player_stats(season: str):
    try:
        data = re.get(f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}').json()
        for item in data:
            create_stat(item)
    except Exception as e:
        print(e)
        exit()