from flask import jsonify, request, Blueprint
from models.player import Player



players_bp = Blueprint('players_bp', __name__, url_prefix='/api')

@players_bp.route('/players', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    players = Player.query.filter(Player.stats.position == position, Player.stats.season == season).all()
    return jsonify(players)
    
