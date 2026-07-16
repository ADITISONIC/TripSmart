"""
ai_summary.py

Generates a human-readable explanation for why a flight
was recommended.
"""

from backend.models import RankedFlight


def generate_summary(
    best: RankedFlight,
    cheapest: RankedFlight,
    fastest: RankedFlight,
    safest: RankedFlight,
    alternatives: list[RankedFlight],
) -> str:

    flight = best.flight
    risk = best.risk

    summary = (
        f"We recommend {flight.airline} {flight.flight_number} "
        f"because it provides the best overall balance of reliability, "
        f"travel time, and price.\n\n"
    )

    summary += (
        f"• Fare: ₹{flight.fare:.0f}\n"
        f"• Duration: {flight.duration_minutes} minutes\n"
        f"• Stops: {flight.stops}\n"
        f"• Risk Score: {risk.total_risk_score}\n"
        f"• Comfort Score: {risk.comfort_score}/100\n\n"
    )

    summary += "Why this flight?\n"

    for reason in risk.reasons[:4]:
        summary += f"✓ {reason}\n"

    summary += "\nComparison:\n"

    if flight.flight_id != cheapest.flight.flight_id:
        diff = flight.fare - cheapest.flight.fare
        summary += (
            f"• It costs ₹{diff:.0f} more than the cheapest option, "
            f"but offers a lower travel risk.\n"
        )
    else:
        summary += "• This is also the cheapest available flight.\n"

    if flight.flight_id != fastest.flight.flight_id:
        diff = flight.duration_minutes - fastest.flight.duration_minutes
        summary += (
            f"• It is {diff} minutes longer than the fastest option "
            f"while providing a better overall balance.\n"
        )
    else:
        summary += "• This is also the fastest available flight.\n"

    if flight.flight_id == safest.flight.flight_id:
        summary += "• It has the lowest risk score among all available flights.\n"

    if alternatives:
        summary += (
            f"\nWe evaluated {len(alternatives) + 1} flight options and "
            "selected this itinerary because it offers the best overall value."
        )

    return summary