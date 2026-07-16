"""
recommender.py

Ranks flights based on user preference and returns
multiple recommendations along with useful statistics.
"""

from typing import List

from backend.models import (
    Flight,
    RankedFlight,
    RecommendResponse,
)

from backend.risk_engine import score_flight
from backend.ai_summary import generate_summary


# ---------------------------------------------------------
# Rank all flights by risk
def overall_score(flight: RankedFlight):

    risk = flight.risk.total_risk_score

    duration = flight.flight.duration_minutes / 60

    fare = flight.flight.fare / 1000

    return (
        risk * 0.5
        + duration * 0.3
        + fare * 0.2
    )


def rank_flights(flights: List[Flight]) -> List[RankedFlight]:

    ranked = []

    for flight in flights:

        ranked.append(
            RankedFlight(
                flight=flight,
                risk=score_flight(flight)
            )
        )

    ranked.sort(
        key=lambda x: (
            x.risk.total_risk_score,
            x.flight.fare,
            x.flight.duration_minutes,
        )
    )

    return ranked


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

def calculate_statistics(

    flights: List[Flight],

    cheapest: RankedFlight,

    fastest: RankedFlight,

):

    return {

        "total_flights": len(flights),

        "average_fare": round(

            sum(f.fare for f in flights) / len(flights),

            2,

        ),

        "lowest_fare": min(f.fare for f in flights),

        "highest_fare": max(f.fare for f in flights),

        "average_duration": round(

            sum(f.duration_minutes for f in flights) / len(flights),

            2,

        ),

        "direct_flights": len(

            [f for f in flights if f.stops == 0]

        ),

        "connecting_flights": len(

            [f for f in flights if f.stops > 0]

        ),

        "cheapest_airline": cheapest.flight.airline,

        "fastest_airline": fastest.flight.airline,

    }


# ---------------------------------------------------------
# Main Recommendation
# ---------------------------------------------------------

def recommend(
    flights: List[Flight],
    preference: str = "best",
) -> RecommendResponse:

    if not flights:
        raise ValueError("No flights available.")

    ranked = rank_flights(flights)

    # -----------------------------------------------------
    # Different recommendation categories
    # -----------------------------------------------------

    cheapest = min(
        ranked,
        key=lambda x: x.flight.fare
    )

    fastest = min(
        ranked,
        key=lambda x: x.flight.duration_minutes
    )

    lowest_risk = min(
        ranked,
        key=lambda x: x.risk.total_risk_score
    )

    # -----------------------------------------------------
    # User Preference
    # -----------------------------------------------------

    if preference == "cheapest":
        best = cheapest

    elif preference == "fastest":
        best = fastest

    elif preference == "lowest_risk":
        best = lowest_risk

    else:
        # Best Overall
        best = min(
    ranked,
    key=overall_score,
)

    # -----------------------------------------------------
    # Alternatives
    # -----------------------------------------------------

    alternatives = [
        flight
        for flight in ranked
        if flight.flight.flight_id != best.flight.flight_id
    ]

    alternatives = alternatives[:3]

    # -----------------------------------------------------
    # Statistics
    # -----------------------------------------------------

    stats = calculate_statistics(
    flights,
    cheapest,
    fastest,
)

    # -----------------------------------------------------
    # AI Explanation
    # -----------------------------------------------------

    explanation = generate_summary(
        best=best,
        cheapest=cheapest,
        fastest=fastest,
        safest=lowest_risk,
        alternatives=alternatives,
    )

    # -----------------------------------------------------
    # Response
    # -----------------------------------------------------

    return RecommendResponse(

        best_overall=best,

        cheapest=cheapest,

        fastest=fastest,

        lowest_risk=lowest_risk,

        recommended=best,

        alternatives=alternatives,

        statistics=stats,

        explanation=explanation,
    )