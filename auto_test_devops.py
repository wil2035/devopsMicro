import requests


from constants import API_KEY

def test_post_data():
   url = 'http://localhost/Devops'
   data = {
      "message": "this is a test",
      "to": "Wilmer",
      "from": "Rita Asturia",
      "timeToLifeSec": "60"
   }
   headers = {'X-Parse-REST-API-Key': API_KEY}
   response = requests.post(url, json=data, headers=headers)
   assert response.status_code == 200
