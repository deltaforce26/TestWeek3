import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_404(client):
    response = client.get('/vyuuyv')
    assert response.status_code == 404


def test_get_players_by_position(client):
    response = client.post('/api/players?position=PG')
    assert response.status_code == 405
    response = client.get('/api/players')
    assert response.json == {"error": "Position is required"}
    assert response.status_code == 400
    response = client.get('/api/players?position=PG')
    assert response.status_code == 200
