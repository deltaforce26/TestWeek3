from db import db
from models.player_stats import Player_stats


def create_stat(data: dict) -> dict:
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
        )
        db.session.add(new_stats)
        db.session.commit()
        # print(f"Committed stats for season {data.get('season')}: {new_stats.to_dict()}")
        return new_stats.to_dict()
    except Exception as e:
        db.session.rollback()
        print('error', e)
        return {"error": str(e)}