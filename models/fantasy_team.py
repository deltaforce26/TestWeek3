from db import db


class FantasyTeam(db.Model):
    __tablename__ = 'fantasy_team'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), unique=True, nullable=False)
    player_stats = db.relationship('Player_stats', back_populates='fantasy_team')