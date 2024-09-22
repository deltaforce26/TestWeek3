from db import db


class FantasyTeam(db.Model):
    __tablename__ = 'fantasy_team'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=True)
    two_percent = db.Column(db.Float, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    team_ppg_ratio = db.Column(db.Float, nullable=True)
    collective_atr = db.Column(db.Float, nullable=True)
    player_stats = db.relationship('Player_stats', back_populates='fantasy_team')


    def to_dict_with_players(self):
        return {
            'team_name': self.team_name,
            'player_stats': [player_stat.to_dict() for player_stat in self.player_stats]
        }


    def to_dict(self):
        return {
            'team_name': self.team_name,
            'points': self.points,
            'two_percent': self.two_percent,
            'three_percent': self.three_percent,
            'team_ppg_ratio': self.team_ppg_ratio,
            'collective_atr': self.collective_atr,
        }