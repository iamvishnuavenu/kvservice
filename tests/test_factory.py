from kvservice import create_app
import json

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
   
def test_get_all(client):
    response = client.get('/api/vi/resource/kv/')
    data = json.loads(response.data)
    assert data['a'] == "VAL1"
    assert data['b'] == "VAL2"

def test_post(client):
    response = client.post('/api/vi/resource/kv/?x=new_val')
    resp1 = json.loads(response.data)
    response = client.get('/api/vi/resource/kv/')
    resp2 = json.loads(response.data)
    assert resp1['x'] == resp2['x']  # checking if new key exist x=new_val

def test_delete(client):
    response = client.post('/api/vi/resource/kv/?x=new_val')
    resp1 = json.loads(response.data)
    assert resp1['x'] == 'new_val'
    # deleting
    response = client.delete('/api/vi/resource/kv/?key=x')
    resp2 = json.loads(response.data)
    assert 'x' not in resp2 # x not in inside the kv