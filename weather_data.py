#Data COllection and Extraction
import requests

API_KEY = '5265a2887b5dc0ed4300a9e916958aff'  
CITY = 'Helsinki,FI'  

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(url)
data = response.json()

# Print some parts of the data to see the structure
print(data)

#Transforming the data
from datetime import datetime

data = {
    'coord': {'lon': 24.9355, 'lat': 60.1695},
    'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
    'main': {'temp': 5.17, 'feels_like': 1.25, 'temp_min': 3.76, 'temp_max': 6.6, 'pressure': 1006, 'humidity': 86},
    'wind': {'speed': 5.66, 'deg': 200},
    'clouds': {'all': 75},
    'sys': {'country': 'FI', 'sunrise': 1742875590, 'sunset': 1742921148},
    'name': 'Helsinki'
}

# Convert Unix timestamps to human-readable datetime
sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
sunset_time = datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

# Calculate temperature range
temp_range = data['main']['temp_max'] - data['main']['temp_min']

# Create transformed data
transformed_data = {
    'city': data['name'],
    'temperature': data['main']['temp'],
    'temperature_range': temp_range,
    'humidity': data['main']['humidity'],
    'wind_speed': data['wind']['speed'],
    'weather_description': data['weather'][0]['description'],
    'sunrise': sunrise_time,
    'sunset': sunset_time
}

print(transformed_data)

#Data Loading

