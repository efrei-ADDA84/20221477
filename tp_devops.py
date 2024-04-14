import os
import requests
import json

from flask import Flask, request

app = Flask(__name__)

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route('/')
def index():
    args = request.args
    
    lat = args['lat']
    lon = args['lon']
    

    if 'API_KEY' in os.environ:
        api_key = os.environ['API_KEY']  
        print("La clé API est déclarée:", api_key)  
    else:
        return "La clé API n'a pas été déclarée."

    weather_data = get_weather(lat, lon, api_key)
    
    return json.dumps(weather_data)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
