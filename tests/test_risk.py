from backend.models import Flight
from backend.risk_engine import score_flight


def test_direct_flight_low_risk():

    flight = Flight(
        flight_id="F1",
        airline="IndiGo",
        flight_number="6E101",
        departure_airport="MAA",
        arrival_airport="DEL",
        departure_time="08:00",
        arrival_time="10:45",
        duration_minutes=165,
        stops=0,
        layover_minutes=0,
        fare=5200,
        status="scheduled",
    )

    risk = score_flight(flight)

    assert risk.total_risk_score < 10
    assert risk.comfort_score == 100

def test_tight_layover_high_risk():

    flight = Flight(
        flight_id="F2",
        airline="Air India",
        flight_number="AI101",
        departure_airport="MAA",
        arrival_airport="DEL",
        departure_time="09:00",
        arrival_time="14:00",
        duration_minutes=300,
        stops=1,
        layover_minutes=30,
        fare=4200,
        status="scheduled",
    )

    risk = score_flight(flight)

    assert risk.layover_risk == 25
    assert risk.total_risk_score > 50

def test_night_flight():

    flight = Flight(
        flight_id="F3",
        airline="Vistara",
        flight_number="UK222",
        departure_airport="MAA",
        arrival_airport="DEL",
        departure_time="23:15",
        arrival_time="03:30",
        duration_minutes=255,
        stops=0,
        layover_minutes=0,
        fare=5100,
        status="scheduled",
    )

    risk = score_flight(flight)

    assert risk.late_departure_risk == 20