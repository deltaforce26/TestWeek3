from ..db import db


class Stats(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    games = db.Column(db.Integer, nullable=False)
    two_percent = db.Column(db.Float, nullable=False)
    three_percent = db.Column(db.Float, nullable=False)
    atr = db.Column(db.Float, nullable=False)
    ppg_ratio = db.Column(db.Float, nullable=False)
    player_id =  db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.relationship('Player', back_populates='stats')