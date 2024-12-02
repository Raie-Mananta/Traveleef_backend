from multiprocessing.managers import Array

flight_dto = {
    "type": object,
    "properties": {
        "departure_airport": {
            "name": {"type": "string", "minLength": 1},
            "id": {"type": "string", "minLength": 1},
            "time": {"type": "string", "minLength": 1}
        },

        "arrival_airport": {
            "name": {"type": "string", "minLength": 1},
            "id": {"type": "string", "minLength": 1},
            "time": {"type": "string", "minLength": 1}
        },

        "duration": {"type": "int", "minLength": 1},
        "airplane": {"type": "string", "minLength": 1},
        "airline": {"type": "string", "minLength": 1},
        "travel_class": {"type": "string", "minLength": 1},
        "flight_number": {"type": "string", "minLength": 1},
        "extensions": {"type": Array(), "minLength": 1},
        "legroom": {"type": "string", "minLength": 1},
        "overnight": {"type": bool},
        "often_delayed_by_over_30_min": {"type": bool},
    },
    "required": ["departure_airport", "arrival_airport", "duration", "airplane"],
    "additionalProperties": False
}