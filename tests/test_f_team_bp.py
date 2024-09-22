import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client



def test_create_team(client):
    response = client.get('/api/teams', json={"team_name":"kobe","player_ids": [6, 7, 8, 9, 10]})
    assert response.status_code == 405

    response = client.post('/api/teams', json={})
    assert response.json == {'error': 'No data'}
    assert response.status_code == 400

    response = client.post('/api/teams', json={"player_ids": [6, 7, 8, 9, 10]})
    assert response.json == {'error': 'team name is required'}
    assert response.status_code == 400

    response = client.post('/api/teams', json={"team_name":"shubulu", "player_ids": [6, 7, 8, 9]})
    assert response.json == {'error': 'invalid number of players'}
    assert response.status_code == 400

    response = client.post('/api/teams', json={"team_name":"kobe","player_ids": [6, 7, 8, 9, 10]})
    assert response.json == {'team': 'kobe', 'with player_ids':[6, 7, 8, 9, 10]}
    assert response.status_code == 201






def test_edit_team(client):
    response = client.get('/api/teams', json={"team_name":"kobe","player_ids": [6, 7, 8, 9, 10]})
    assert response.status_code == 405

    response = client.put('/api/teams/0', json={"team_name":"kobe","player_ids": [6, 7, 8, 9, 10]})
    assert response.json == {'error': 'invalid team id'}
    assert response.status_code == 400

    response = client.put('/api/teams/3', json={})
    assert response.json == {'error': 'must have at least 5 players'}
    assert response.status_code == 400

    response = client.put('/api/teams/3', json={"team_name":"kobe","player_ids": [6, 7, 8, 9]})
    assert response.json == {'error': 'must have at least 5 players'}
    assert response.status_code == 400

    response = client.put('/api/teams/4000', json={"team_name":"kobe","player_ids": [6, 7, 8, 9, 10]})
    assert response.json == {'error': 'team not found'}
    assert response.status_code == 404

    response = client.put('/api/teams/2', json={"team_name": "lql","player_ids": [6, 7, 8, 9, 10]})
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.get_json()}")
    assert response.json == {'team': 'lql', 'with player_ids':[6, 7, 8, 9, 10]}
    assert response.status_code == 200







def test_get_team(client):
    response = client.post('/api/teams/1')
    assert response.status_code == 405

    response = client.get('/api/teams/0')
    assert response.json == {'error': 'invalid team id'}
    assert response.status_code == 400

    response = client.get('/api/teams/9000')
    assert response.json == {'error': 'team not found'}
    assert response.status_code == 404

    response = client.get('/api/teams/3')
    assert response.status_code == 200



def test_delete_team(client):
    response = client.post('/api/teams/1',)
    assert response.status_code == 405

    response = client.delete('/api/teams/0')
    assert response.json == {'error': 'invalid team id'}
    assert response.status_code == 400

    response = client.delete('/api/teams/9000')
    assert response.json == {'error': 'team not found'}
    assert response.status_code == 404

    response = client.delete('/api/teams/3')
    assert response.json == {'success': True}
    assert response.status_code == 200
