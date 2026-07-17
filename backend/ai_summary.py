import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(
    best,
    cheapest,
    fastest,
    safest,
    alternatives,
):
    """
    Uses Gemini to generate a natural-language recommendation
    based on the recommendation engine output.
    """

    prompt = f"""
You are TripSmart, an AI travel assistant.

A user searched for flights.

Recommended Flight:
Airline: {best.flight.airline}
Flight Number: {best.flight.flight_number}
Fare: ₹{best.flight.fare}
Duration: {best.flight.duration_minutes} minutes
Stops: {best.flight.stops}
Risk Score: {best.risk.total_risk_score}
Comfort Score: {best.risk.comfort_score}

Cheapest Flight:
{cheapest.flight.airline} ({cheapest.flight.flight_number})
Fare: ₹{cheapest.flight.fare}

Fastest Flight:
{fastest.flight.airline} ({fastest.flight.flight_number})
Duration: {fastest.flight.duration_minutes} minutes

Safest Flight:
{safest.flight.airline} ({safest.flight.flight_number})
Risk Score: {safest.risk.total_risk_score}

Reasons for recommendation:
{", ".join(best.risk.reasons)}

Write a travel recommendation in 180-250 words.

The response should include:

1. A short recommendation paragraph.
2. Explain why this flight was selected.
3. Compare it with the cheapest flight.
4. Compare it with the fastest flight.
5. Mention any trade-offs in price, duration, or connections.
6. Mention whether it is suitable for business travelers or leisure travelers.
7. End with one final recommendation sentence.

Write naturally like a travel advisor.
Do not use markdown.
"""

    try:
        response = client.models.generate_content(

    model="gemini-2.0-flash-lite",

    contents=prompt,

)
        print(response.text)      # Debug
        return response.text
    except Exception as e:
        print(e)                  # VERY IMPORTANT
        return f"Gemini Error: {e}"