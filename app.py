from flask import Flask
from bluprints.fantasy_taems_bp import fantasy_teams_bp
from bluprints.players_bp import players_bp
from bluprints.stats_bp import stats_bp
from db import db
from services.api_service import get_player_stats
from services.calc_sevice import atr_calc

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)




with app.app_context():
    db.drop_all()
    db.create_all()

    print("Fetching data for 2022...")
    get_player_stats('2022')
    print("Fetching data for 2023...")
    get_player_stats('2023')
    print("Fetching data for 2024...")
    get_player_stats('2024')




app.register_blueprint(players_bp)
app.register_blueprint(fantasy_teams_bp)
app.register_blueprint(stats_bp)



if __name__ == '__main__':
    # main()
    app.run(debug=False)
