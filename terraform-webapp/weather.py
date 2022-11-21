from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "34ae2e21b466cbe4491bb0c1bcb50a1c"

@app.route('/')
def index():
    return 'base path!'

@app.route('/<string:city>/')
def weather(city):

    url="https://api.openweathermap.org/data/2.5/weather"
    params = dict(
        q=city ,
        appid= API_KEY,
    )
    response = requests.get(url=url,params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)