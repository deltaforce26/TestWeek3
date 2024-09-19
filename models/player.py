# from models.player_stats import Stats
# from db import db
#
#
# class Player(db.Model):
#     __tablename__ = 'players'
#     id = db.Column(db.Integer, primary_key=True)
#     player_id = db.Column(db.Integer, unique=True, nullable=False)
#     name = db.Column(db.String(80), nullable=True)
#     stats = db.relationship('Stats', back_populates='player')
#
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'player_id': self.player_id,
#             'name': self.name
#         }
#
