from models.player_stats import Player_stats

# calculates the Assist-to-Turnover Ratio
def atr_calc(assists, turnovers):
    if assists == 0 or turnovers == 0:
        return 0
    if assists is None or turnovers is None:
        return 0
    return round(assists / turnovers, 2)


# calculates points per game ratio for a given player
def ppg_ratio_calc(player, data):
    players = list(filter(lambda item: item['position'] == player['position'], data))
    avg = round(sum(player['points'] for player in players) / len(players), 2)
    ppg_ratio = round(player['points'] / avg, 2)
    return ppg_ratio








