import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client



def test_compare_fantasy_teams(client):
    response = client.post('/api/stats/compare?team1=jake&team2=lwl')
    assert response.status_code == 405
    response = client.get('/api/stats/compare?team1=kobe')
    assert response.json == {'error': 'Please enter at least two teams'}
    assert response.status_code == 400
    response = client.get('/api/stats/compare?team1=jake&team2=lwl')
    assert response.status_code == 200
