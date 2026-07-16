from backend.models import Flight
from backend.recommender import recommend

def test_best_overall():

    flights = [

        Flight(
            flight_id="1",
            airline="A",
            flight_number="A1",
            departure_airport="MAA",
            arrival_airport="DEL",
            departure_time="08:00",
            arrival_time="10:30",
            duration_minutes=150,
            stops=0,
            layover_minutes=0,
            fare=5400,
            status="scheduled",
        ),

        Flight(
            flight_id="2",
            airline="B",
            flight_number="B1",
            departure_airport="MAA",
            arrival_airport="DEL",
            departure_time="22:30",
            arrival_time="03:00",
            duration_minutes=280,
            stops=1,
            layover_minutes=35,
            fare=4300,
            status="scheduled",
        ),

    ]

    result = recommend(flights)

    assert result.recommended.flight.flight_id == "1"

def test_cheapest():

    flights = [
        Flight(
            flight_id="1",
            airline="A",
            flight_number="A1",
            departure_airport="MAA",
            arrival_airport="DEL",
            departure_time="08:00",
            arrival_time="10:00",
            duration_minutes=150,
            stops=0,
            layover_minutes=0,
            fare=6000,
            status="scheduled",
        ),
        Flight(
            flight_id="2",
            airline="B",
            flight_number="B1",
            departure_airport="MAA",
            arrival_airport="DEL",
            departure_time="09:00",
            arrival_time="12:30",
            duration_minutes=210,
            stops=0,
            layover_minutes=0,
            fare=4000,
            status="scheduled",
        ),
    ]

    result = recommend(flights, preference="cheapest")

    assert result.recommended.flight.fare == 4000

