from flask import Flask
from markupsafe import escape
import requests
import json

app = Flask(__name__)

@app.route("/weather/<city>", methods=["GET"])
def weather(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "c"}

    headers = {
        "x-rapidapi-key": "ad422ab043msha304f4c72501285p13bbdcjsn45261c82a9d1",
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(type(response.json()))
    json_string = json.dumps(response.json(), indent=4)
    return f"{json_string}"


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'opa {escape(username)}'
