import app
import requests
import json
from flask import jsonify

def mock_weather(a, b, c):
    data = {
        "data": {
            "current": {
                "weather": {
                    "hu": 39,
                    "ws": 30,
                    "tp": 12,
                }
            }
        }
    } 
    return data

def mock_request():
    {
        "method": 'POST'
    }
   

def test_hello_world(api):
    res = api.get('/')
    assert res.status == '200 OK'
    assert res.data == b'Hello World'

def test_weather(monkeypatch):
    monkeypatch.setattr(app, "data_request", mock_weather)
    weather = json.loads(app.weather('UK', 'England', 'London'))
    assert 30 == weather["wind_speed"]

def test_user_info(monkeypatch):
    resp = requests.post('http://localhost:5000/user')
    assert resp.response == 'user info'
