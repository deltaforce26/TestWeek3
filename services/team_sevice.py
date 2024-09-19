from db import db
from models.fantasy_team import FantasyTeam
from models.player_stats import Player_stats


def create_fantasy_team(team_name, player_ids):
    new_team = FantasyTeam(
        team_name=team_name,
        player_stats=get_players_by_id(player_ids)
    )
    try:
        db.session.add(new_team)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        exit(e)



def get_players_by_id(ids):
    players = []
    for player_id in ids:
        player = db.session.query(Player_stats).filter_by(id=player_id).first()
        players.append(player)
    return players
