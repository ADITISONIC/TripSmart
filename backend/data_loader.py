import json

from backend.models import Flight


def load_flights():

    with open("backend/sample_data.json", "r") as file:
        data = json.load(file)

    return [Flight(**flight) for flight in data]


def search_flights(origin: str, destination: str):

    flights = load_flights()

    return [
        flight
        for flight in flights
        if flight.departure_airport.upper() == origin.upper()
        and flight.arrival_airport.upper() == destination.upper()
    ]