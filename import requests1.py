import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/alerts')
def get_weather_alerts():
    
    api_url = 'https://api.weatherbit.io/v2.0/alerts'
    params = {
        'lat': '39.75895',
        'lon': '-84.19161',
        'key': '3a01582fbcd64166afcfbfa51f3f6555'
    }
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/alerts')
def get_weather_alerts():
    
    api_url = 'https://api.weatherbit.io/v2.0/alerts'
    params = {
        'lat': '39.75895',
        'lon': '-84.19161',
        'key': '3a01582fbcd64166afcfbfa51f3f6555'
    }

    try:
        
        response = requests.get(api_url, params=params)
        response.raise_for_status()  

        
        data = response.json()

        
        return jsonify(data)
    except requests.RequestException as e:
        
        error_message = f'Error fetching data: {str(e)}'
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)

    try:
        
        response = requests.get(api_url, params=params)
        response.raise_for_status()  

        
        data = response.json()

        
        return jsonify(data)
    except requests.RequestException as e:
        
        error_message = f'Error fetching data: {str(e)}'
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
