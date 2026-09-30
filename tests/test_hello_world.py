import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def test_hello_world_i_am_mk():
    with app.test_client() as client:
        response = client.get('/hello_world_i_am_mk')
        assert response.status_code == 200
        data = response.get_json()
        assert data == {'message': 'Hello World I am MK'}