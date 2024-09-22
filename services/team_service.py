from db import db
from models.fantasy_team import FantasyTeam
from models.player_stats import Player_stats


def get_players_by_id(ids: list) -> list:
    players = []
    for player_id in ids:
        try:
            player = db.session.query(Player_stats).filter_by(id=player_id).first()
            players.append(player)
        except Exception as e:
            print(f'An exception occurred: {e}')
    return players



def create_fantasy_team(team_name: str, player_ids: list):
    new_team = FantasyTeam(
        team_name = team_name,
        player_stats = get_players_by_id(player_ids)
    )
    new_team.two_percent = collective_percentage(new_team, 'two_percent')
    new_team.three_percent = collective_percentage(new_team, 'three_percent')
    new_team.team_ppg_ratio = collective_ppg(new_team)
    new_team.points = collective_points(new_team)
    new_team.collective_atr = collective_atr(new_team)
    try:
        db.session.add(new_team)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f'An exception occurred: {e}')
        exit(e)


def collective_percentage(team: FantasyTeam, percent: str):
    ctp = 0
    valid_players_count = 0
    for player in team.player_stats:
        percentage = getattr(player, percent, None)
        if percentage is not None:
            ctp += percentage
            valid_players_count += 1
    try:
        return round(ctp / len(team.player_stats), 2) if valid_players_count > 0 else 0
    except ZeroDivisionError as e:
        print(f'An exception occurred: {e}')
        return 0




def collective_ppg(team: FantasyTeam):
    ppg = 0
    valid_players_count = 0
    for player in team.player_stats:
        if player.ppg_ratio:
            ppg += player.ppg_ratio
            valid_players_count += 1
    try:
        return round(ppg / len(team.player_stats), 2) if valid_players_count > 0 else 0
    except ZeroDivisionError as e:
        print(f'An exception occurred: {e}')
        return 0



def collective_points(team: FantasyTeam):
    points = 0
    valid_players_count = 0
    for player in team.player_stats:
        if player.points:
            points += player.points
            valid_players_count += 1
    return points


def collective_atr(team: FantasyTeam):
    atr = 0
    valid_players_count = 0
    for player in team.player_stats:
        if player.atr:
            atr += player.atr
            valid_players_count += 1
    try:
        return round(atr / len(team.player_stats), 2) if valid_players_count > 0 else 0
    except ZeroDivisionError as e:
        print(f'An exception occurred: {e}')


def edit_fantasy_team(team: FantasyTeam ,team_name: str, player_ids: list):
    team.team_name = team_name
    team.player_stats = get_players_by_id(player_ids)
    try:
        db.session.commit()
        return team
    except Exception as e:
        db.session.rollback()
        print(f'An exception occurred: {e}')
        return team
