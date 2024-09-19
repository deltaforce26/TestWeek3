from db import db


class Player_stats(db.Model):
    __tablename__ = 'player_stats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    team = db.Column(db.String(10), nullable=True)
    position = db.Column(db.String(10), nullable=True)
    season = db.Column(db.String(10), nullable=True)
    points = db.Column(db.Integer, nullable=True)
    games = db.Column(db.Integer, nullable=True)
    two_percent = db.Column(db.Float, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    atr = db.Column(db.Float, nullable=True)
    ppg_ratio = db.Column(db.Float, nullable=True)
    fantasy_team_id = db.Column(db.Integer, db.ForeignKey('fantasy_team.id'))
    fantasy_team = db.relationship('FantasyTeam', back_populates='player_stats')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'team': self.team,
            'position': self.position,
            'season': self.season,
            'points': self.points,
            'games': self.games,
            'two_percent': self.two_percent,
            'three_percent': self.three_percent,
            'atr': self.atr,
            'ppg_ratio': self.ppg_ratio,
        }