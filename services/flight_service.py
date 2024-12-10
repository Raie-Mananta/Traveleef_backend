import requests
from shared.dto.mappers.flight_mapper import map_flight_response
from domain.repositories.flight_repository import FlightRepository

class FlightService:
    @staticmethod
    def search_flights(filters):
        response = FlightRepository.fetch_flights(filters)
        return map_flight_response(response)