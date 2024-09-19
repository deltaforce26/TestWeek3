from flask import jsonify, request, Blueprint



stats_bp = Blueprint('stats_bp', __name__, url_prefix='/api')



# compares two or more fantasy teams
@stats_bp.route('/stats/compare', methods=['GET'])
def compare_fantasy_teams():
    teams = request.args.to_dict()
    pass