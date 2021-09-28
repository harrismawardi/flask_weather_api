import requests
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import Weather

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# mock user interface from the front end. 
def get_user_information():
    country = input('what country do you want?')
    state = input('what state do you want?')
    city = input('what city do you want?')
    print(weather(country, state, city))


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/weather/<string:country>/<string:state>/<string:city>')
def weather(country, state, city):
    print(country, state, city)
    url = f"https://api.airvisual.com/v2/city?city={city}&country={country}&state={state}&key=4374ac90-b6ff-4b8c-a86e-809564970414"
    resp = requests.get(url)
    data = resp.json()
    weather_data = Weather(data["data"]["current"])
    weather_json = json.dumps(weather_data.__dict__)
    return weather_json

@app.route('/user', methods=['POST', 'GET'])
def user_info():
    if request.method == 'GET':
        return 'user info', 200
    elif request.method == 'POST':
        body = request.get_json()
        return f'you have made a new account, {body["name"]}', 201

if __name__ == "__main__":
    app.run(debug=True)