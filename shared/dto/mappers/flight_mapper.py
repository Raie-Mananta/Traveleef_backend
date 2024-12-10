def map_flight_response(api_response):
    flights = []
    for flight in api_response.get('flights', []):
        mapped_flight = {
            "departure_airport": {
                "name": flight.get("departure_airport_name"),
                "id": flight.get("departure_airport_id"),
                "time": flight.get("departure_time")
            },
            "arrival_airport": {
                "name": flight.get("arrival_airport_name"),
                "id": flight.get("arrival_airport_id"),
                "time": flight.get("arrival_time")
            },
            "duration": flight.get("duration"),
            "airplane": flight.get("airplane"),
            "airline": flight.get("airline"),
            "travel_class": flight.get("travel_class"),
            "flight_number": flight.get("flight_number"),
            "extensions": flight.get("extensions", []),
            "legroom": flight.get("legroom"),
            "overnight": flight.get("overnight"),
            "often_delayed_by_over_30_min": flight.get("often_delayed")
        }
        flights.append(mapped_flight)
    return flights