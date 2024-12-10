flight_dto = {
    "type": "object",
    "properties": {
        "departure_airport": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "minLength": 1},
                "id": {"type": "string", "minLength": 1},
                "time": {"type": "string", "minLength": 1}
            },
            "required": ["name", "id", "time"]
        },
        "arrival_airport": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "minLength": 1},
                "id": {"type": "string", "minLength": 1},
                "time": {"type": "string", "minLength": 1}
            },
            "required": ["name", "id", "time"]
        },
        "duration": {"type": "integer", "minimum": 1},
        "airplane": {"type": "string", "minLength": 1},
        "airline": {"type": "string", "minLength": 1},
        "travel_class": {"type": "string", "minLength": 1},
        "flight_number": {"type": "string", "minLength": 1},
        "extensions": {"type": "array", "items": {"type": "string"}},
        "legroom": {"type": "string", "minLength": 1},
        "overnight": {"type": "boolean"},
        "often_delayed_by_over_30_min": {"type": "boolean"}
    },
    "required": ["departure_airport", "arrival_airport", "duration", "airplane", "airline"],
    "additionalProperties": False
}