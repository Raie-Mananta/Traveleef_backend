import requests
from domain.kernel.config import Config

API_KEY = Config.API_KEY
API_URL = Config.API_URL

class FlightRepository:
    @staticmethod
    def fetch_flights(filters):
        params = {
            "engine": "google_flights",
            "api_key": API_KEY,
            **filters
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()