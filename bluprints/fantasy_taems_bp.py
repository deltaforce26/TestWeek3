from flask import jsonify, request, Blueprint

from db import db
from models.fantasy_team import FantasyTeam
from services.team_service import create_fantasy_team, get_players_by_id, edit_fantasy_team

fantasy_teams_bp = Blueprint('fantasy_teams_bp', __name__, url_prefix='/api')


@fantasy_teams_bp.route('/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data'}), 400
    team_name = data.get('team_name')
    if not team_name:
        return jsonify({'error': 'team name is required'}), 400
    already_exist = FantasyTeam.query.filter_by(team_name=team_name).first()
    if already_exist:
        return jsonify({'error': 'A team  with that name already exist'}), 400
    player_ids = data.get('player_ids')
    if len(player_ids) != 5:
        return jsonify({'error': 'invalid number of players'}), 400
    create_fantasy_team(team_name, player_ids)
    return jsonify({'team': team_name, 'with player_ids':player_ids}), 201




@fantasy_teams_bp.route('/teams/<int:team_id>', methods=['PUT'])
def edit_team(team_id):
    if team_id < 1:
        return jsonify({'error': 'invalid team id'}), 400
    data = request.get_json()
    player_ids = data.get('player_ids')
    if not data or len(player_ids) != 5:
        return jsonify({'error': 'must have at least 5 players'}), 400
    team = FantasyTeam.query.get(team_id)
    if not team:
        return jsonify({'error': 'team not found'}), 404
    new_team_name = data.get('team_name')
    if new_team_name:
        already_exist = FantasyTeam.query.filter_by(team_name=new_team_name).first()
        if already_exist:
            return jsonify({'error': 'A team  with that name already exist'}), 400
    edit_fantasy_team(team, new_team_name, player_ids)
    return jsonify({'team': team.team_name, 'with player_ids':player_ids}), 200





@fantasy_teams_bp.route('/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    if team_id < 1:
        return jsonify({'error': 'invalid team id'}), 400
    team = FantasyTeam.query.get(team_id)
    if not team:
        return jsonify({'error': 'team not found'}), 404
    db.session.delete(team)
    db.session.commit()
    return jsonify({'success': True}), 200




@fantasy_teams_bp.route('/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    if team_id < 1:
        return jsonify({'error': 'invalid team id'}), 400
    team = FantasyTeam.query.get(team_id)
    if not team:
        return jsonify({'error': 'team not found'}), 404
    return jsonify(team.to_dict_with_players()), 200

