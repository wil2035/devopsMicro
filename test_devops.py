import json

def test_devops_not_found(client):
    response = client.post('/Devops', data=json.dumps({'message': 'Hello world!'}), content_type='application/json')
    assert response.status_code == 404