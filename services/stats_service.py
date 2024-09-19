from db import db
from models.stats import Stats


def create_stat(data: dict) -> dict:
    try:
        new_stats = Stats(
            age=data.get('age'),
            team=data.get('team'),
            position=data.get('position'),
            season=data.get('season'),
            points=data.get('points'),
            games=data.get('games'),
            two_percent=data.get('twoPercent'),
            three_percent=data.get('threePercent'),
            player_id=data.get('player_id'),
        )
        db.session.add(new_stats)
        db.session.commit()
        return new_stats.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}