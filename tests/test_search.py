import json


def test_sample_data_exists():

    with open("backend/sample_data.json") as f:

        flights = json.load(f)

    assert len(flights) >= 10

def test_route_exists():

    with open("backend/sample_data.json") as f:

        flights = json.load(f)

    result = [

        f

        for f in flights

        if f["departure_airport"] == "MAA"

        and f["arrival_airport"] == "DEL"

    ]

    assert len(result) > 0