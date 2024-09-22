from db import db
from models.player_stats import Player_stats
from services.calc_service import atr_calc, ppg_ratio_calc


def create_stats(data: list[dict]):
    for player in data:
        ppg = ppg_ratio_calc(player, data)
        create_stat(player, ppg)



def create_stat(data: dict, ppg_ratio) -> dict:
    try:
        new_stats = Player_stats(
            name=data.get('playerName'),
            age=data.get('age'),
            assists=data.get('assists'),
            turnovers=data.get('turnovers'),
            team=data.get('team'),
            position=data.get('position'),
            season=data.get('season'),
            points=data.get('points'),
            games=data.get('games'),
            two_percent=data.get('twoPercent'),
            three_percent=data.get('threePercent'),
            atr=atr_calc(data.get('assists'), data.get('turnovers')),
            ppg_ratio=ppg_ratio
        )
        db.session.add(new_stats)
        db.session.commit()
        return new_stats.to_dict()
    except Exception as e:
        db.session.rollback()
        print('error', e)
        return {"error": str(e)}