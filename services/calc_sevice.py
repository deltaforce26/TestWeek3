from models.player_stats import Player_stats


def atr_calc(id):
    assits = Player_stats.query.with_entities(Player_stats.assists).filter(Player_stats.id == id).all()
    print(assits)



