from models.player import Player
from db import db



def create_player(data: dict) -> dict:
    try:
        new_player = Player(
            player_id=data['playerId'],
            name=data['playerName']
        )
        db.session.add(new_player)
        db.session.commit()
        return new_player.to_dict_with_players()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}