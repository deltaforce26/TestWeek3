from ..db import db


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    stats = db.relationship('Stats', back_populates='player')


    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'name': self.name,
            'age': self.age
        }

