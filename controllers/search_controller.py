from flask import Blueprint, request, jsonify
from services.flight_service import FlightService

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_flights():
    try:
        filters = request.get_json()
        flights = FlightService.search_flights(filters)
        return jsonify(flights)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@search_bp.route('/search/ecology', methods=['GET'])
def search_ecology_flights():
    try:
        filters = request.get_json()
        filters['emissions'] = True
        flights = FlightService.search_flights(filters)
        return jsonify(flights)
    except Exception as e:
        return jsonify({"error": str(e)}), 500