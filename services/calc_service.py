from models.player_stats import Player_stats


def atr_calc(id):
    assists = Player_stats.query.with_entities(Player_stats.assists).filter(Player_stats.id == id).all()
    turnovers = Player_stats.query.with_entities(Player_stats.turnovers).filter(Player_stats.id == id).all()
    if len(assists) == 0 and len(turnovers) == 0:
        return 0
    total_assists = [row[0] for row in assists]
    total_turnovers = [row[0] for row in turnovers]
    if sum(total_assists) == 0 or sum(total_turnovers) == 0:
        return 0
    atr = (sum(total_assists) / sum(total_turnovers))
    print(assists)
    return round(atr, 2)


def ppg_ratio_calc(id):




