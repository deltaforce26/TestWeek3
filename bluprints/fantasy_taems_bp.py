from flask import jsonify, request, Blueprint



fantasy_teams_bp = Blueprint('fantasy_teams_bp', __name__, url_prefix='/api')


@fantasy_teams_bp.route('/teams', methods=['POST'])
def create_team():
    pass



@fantasy_teams_bp.route('/teams/<team_id:int>', methods=['PUT'])
def edit_team(team_id):
    pass


@fantasy_teams_bp.route('/teams/<team_id:int>', methods=['DELETE'])
def delete_team(team_id):
    pass



@fantasy_teams_bp.route('/teams/<team_id:int>', methods=['GET'])
def get_team(team_id):
    pass

