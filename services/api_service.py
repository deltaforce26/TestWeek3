import json
import requests as re



def get_player_stats(season: str):
    try:
        data = re.get(f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}').json()
        return data
    except Exception as e:
        print(e)
        exit()




def write_players_to_json(data):
    with open('players.json', 'w') as outfile:
        json.dump(data, outfile)



def get_players_from_json(file_path: str) -> list[dict]:
    with open(file_path, 'r') as infile:
        data = json.load(infile)
        return data


