import os
import requests

# Fonction pour obtenir les données météorologiques à partir de l'API OpenWeatherMap
def get_weather(latitude, longitude):
    api_key = os.environ.get('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The current weather is {weather_description} with a temperature of {temperature}°C"
    else:
        return "Failed to fetch weather data"

if __name__ == "__main__":
    latitude = os.environ.get('LAT')
    longitude = os.environ.get('LONG')
    print(get_weather(latitude, longitude))