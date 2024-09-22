from flask import jsonify, request, Blueprint

from models.fantasy_team import FantasyTeam

stats_bp = Blueprint('stats_bp', __name__, url_prefix='/api')



# compares two or more fantasy teams
@stats_bp.route('/stats/compare', methods=['GET'])
def compare_fantasy_teams():
    teams = list(request.args.to_dict().values())
    if len(teams) < 2:
        return jsonify({'error': 'Please enter at least two teams'}), 400
    f_teams = FantasyTeam.query.filter(FantasyTeam.team_name.in_(teams)).all()
    if len(f_teams) < 1:
        return jsonify({'error': 'No teams were found'}), 400
    return jsonify(sorted([f_team.to_dict() for f_team in f_teams], key=lambda team: team['team_ppg_ratio'], reverse=True)), 200
    

