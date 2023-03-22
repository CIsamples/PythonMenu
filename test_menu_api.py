import json
import pytest
from menu_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_menu_item(client):
    response = client.get('/menuapi/item/1')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['name'] == 'Cheeseburger'

def test_get_menu_item_not_found(client):
    response = client.get('/menuapi/item/99')
    data = json.loads(response.data)
    assert response.status_code == 404
    assert data['error'] == 'Item not found'

def test_get_all_menu_items(client):
    response = client.get('/menuapi/items')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 3
    assert data[0]['name'] == 'Cheeseburger'
    assert data[1]['name'] == 'Caesar Salad'
    assert data[2]['name'] == 'Chicken Alfredo'
