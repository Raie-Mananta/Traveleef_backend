import requests
from flask import Blueprint, request, jsonify

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST'])
def search():
    departure_id = request.json.get('departure_id')
    arrival_id = request.json.get('arrival_id')
    outbound_date = request.json.get('outbound_date')
    return_date = request.json.get('return_date') 

    
    API_KEY = "3394251b499b0eb233be82862c94da861aec52cce9bc05a2b94411e7a2252dc8"

    
    api_url = "https://serpapi.com/search"
    params = {
        "engine": "google_flights",
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "api_key": API_KEY
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status() 
        data = response.json()

        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
