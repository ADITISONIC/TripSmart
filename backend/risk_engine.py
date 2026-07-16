"""
risk_engine.py

TripSmart Risk Engine

Calculates:
- Connection Risk
- Layover Risk
- Time Risk
- Duration Risk
- Cost Penalty
- Comfort Score
- Overall Risk Score

Lower overall risk = Better flight
"""

from backend.models import Flight, RiskBreakdown


# -----------------------------------------------------
# Configuration
# -----------------------------------------------------

RISK_PER_STOP = 15

TIGHT_LAYOVER = 45
MEDIUM_LAYOVER = 90

TIGHT_LAYOVER_RISK = 25
MEDIUM_LAYOVER_RISK = 15
SAFE_LAYOVER_RISK = 5

LATE_NIGHT_START = 21
EARLY_MORNING_END = 6
NIGHT_RISK = 20

LONG_DURATION = 180
VERY_LONG_DURATION = 300

MEDIUM_DURATION_RISK = 8
LONG_DURATION_RISK = 15

FARE_DIVISOR = 1000

DIRECT_FLIGHT_BONUS = 10


# -----------------------------------------------------
# Helpers
# -----------------------------------------------------

def departure_hour(time: str) -> int:
    return int(time.split(":")[0])


# -----------------------------------------------------
# Main Risk Function
# -----------------------------------------------------

def score_flight(flight: Flight) -> RiskBreakdown:

    reasons = []

    # ---------------------------------------
    # Connection Risk
    # ---------------------------------------

    stops_risk = flight.stops * RISK_PER_STOP

    if flight.stops == 0:
        reasons.append("Direct flight with no connections.")

    elif flight.stops == 1:
        reasons.append("One stop increases connection risk.")

    else:
        reasons.append(f"{flight.stops} stops increase travel complexity.")

    # ---------------------------------------
    # Layover Risk
    # ---------------------------------------

    layover_risk = 0

    if flight.stops > 0:

        if flight.layover_minutes < TIGHT_LAYOVER:

            layover_risk = TIGHT_LAYOVER_RISK

            reasons.append(
                f"Tight layover ({flight.layover_minutes} mins) may cause missed connections."
            )

        elif flight.layover_minutes < MEDIUM_LAYOVER:

            layover_risk = MEDIUM_LAYOVER_RISK

            reasons.append(
                f"Moderate layover ({flight.layover_minutes} mins)."
            )

        else:

            layover_risk = SAFE_LAYOVER_RISK

            reasons.append(
                f"Comfortable layover ({flight.layover_minutes} mins)."
            )

    # ---------------------------------------
    # Time Risk
    # ---------------------------------------

    hour = departure_hour(flight.departure_time)

    if hour >= LATE_NIGHT_START or hour < EARLY_MORNING_END:

        late_departure_risk = NIGHT_RISK

        reasons.append(
            "Late-night departure may increase fatigue."
        )

    else:

        late_departure_risk = 0

        reasons.append(
            "Convenient daytime departure."
        )

    # ---------------------------------------
    # Duration Risk
    # ---------------------------------------

    if flight.duration_minutes > VERY_LONG_DURATION:

        duration_risk = LONG_DURATION_RISK

        reasons.append(
            f"Very long journey ({flight.duration_minutes} mins)."
        )

    elif flight.duration_minutes > LONG_DURATION:

        duration_risk = MEDIUM_DURATION_RISK

        reasons.append(
            f"Moderately long journey ({flight.duration_minutes} mins)."
        )

    else:

        duration_risk = 0

        reasons.append(
            "Short travel duration."
        )

    # ---------------------------------------
    # Cost Penalty
    # ---------------------------------------

    cost_penalty = round(flight.fare / FARE_DIVISOR, 2)

    if flight.fare < 4000:

        reasons.append("Budget-friendly ticket.")

    elif flight.fare < 5500:

        reasons.append("Reasonably priced.")

    else:

        reasons.append("Premium fare.")

    # ---------------------------------------
    # Comfort Score
    # ---------------------------------------

    comfort_score = 100

    comfort_score -= stops_risk
    comfort_score -= layover_risk
    comfort_score -= late_departure_risk
    comfort_score -= duration_risk

    if flight.stops == 0:
        comfort_score += DIRECT_FLIGHT_BONUS

    comfort_score = max(0, min(100, comfort_score))

    # ---------------------------------------
    # Overall Risk
    # ---------------------------------------

    total_risk = round(
        stops_risk
        + layover_risk
        + late_departure_risk
        + duration_risk
        + cost_penalty,
        2,
    )

    # ---------------------------------------
    # Return
    # ---------------------------------------
    if total_risk < 15:
        rating = "Excellent"
    elif total_risk < 35:
        rating = "Good"
    elif total_risk < 55:
        rating = "Average"
        
    elif total_risk < 75:
        rating = "Poor"
    else:
        rating = "High Risk"

    return RiskBreakdown(

        stops_risk=stops_risk,
        travel_rating=rating,

        layover_risk=layover_risk,

        late_departure_risk=late_departure_risk,

        duration_risk=duration_risk,

        cost_penalty=cost_penalty,

        comfort_score=comfort_score,

        total_risk_score=total_risk,

        reasons=reasons,
    )