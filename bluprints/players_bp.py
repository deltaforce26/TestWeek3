from flask import jsonify, request, Blueprint
from models.player_stats import Player_stats
from services.calc_service import atr_calc

players_bp = Blueprint('players_bp', __name__, url_prefix='/api')

@players_bp.route('/players', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    if not position:
        return jsonify({"error": "Position is required"}), 400
    if not validate_position(position):
        return jsonify({'error': 'Invalid position', 'valid options': 'C, PF, SF, SG, PG'}), 400
    try:
        data = Player_stats.query.filter(Player_stats.position == position.upper())
        if season :
            data = data.filter(Player_stats.season == season)
        players = data.all()
        if not players:
            return jsonify({"message": "No players found"}), 404
        players_list = [player.to_dict() for player in players]
        return jsonify(players_list), 200
    except Exception as e:
        return jsonify({"An error occurred. details": str(e)}), 500
    



def validate_position(position):
    match position.upper():
        case 'PG':
            return True
        case 'SG':
            return True
        case 'SF':
            return True
        case 'PF':
            return True
        case 'C':
            return True
        case _:
            return False
