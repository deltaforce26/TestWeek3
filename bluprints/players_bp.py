from flask import jsonify, request, Blueprint
from models.player_stats import Player_stats

players_bp = Blueprint('players_bp', __name__, url_prefix='/api')

@players_bp.route('/players', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    if not position :
        return jsonify({"error": "Position is required"}), 400
    data = Player_stats.query.filter(Player_stats.position == position)
    if season :
        data = data.filter(Player_stats.season == season)
    players = data.all()
    if not players:
        return jsonify({"message": "No players found"}), 404
    players_list = [player.to_dict() for player in players]
    return jsonify(players_list)
    
