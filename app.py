from flask import Flask
from bluprints.fantasy_taems_bp import fantasy_teams_bp
from bluprints.players_bp import players_bp
from bluprints.stats_bp import stats_bp
from db import db
from services.api_service import get_players

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()
    # get_players('2023')


app.register_blueprint(players_bp)
# app.register_blueprint(fantasy_teams_bp)
# app.register_blueprint(stats_bp)



if __name__ == '__main__':
    app.run(debug=True)
