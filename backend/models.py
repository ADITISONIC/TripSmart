"""
Pydantic models for TripSmart.
"""

from typing import List
from pydantic import BaseModel, Field


# ------------------------------------------------------------------
# Flight Model (Loaded from sample_data.json)
# ------------------------------------------------------------------

class Flight(BaseModel):
    flight_id: str
    airline: str
    flight_number: str

    departure_airport: str
    arrival_airport: str

    departure_time: str
    arrival_time: str

    duration_minutes: int

    stops: int
    layover_minutes: int

    fare: float

    status: str = "scheduled"


# ------------------------------------------------------------------
# SEARCH
# ------------------------------------------------------------------

class SearchRequest(BaseModel):
    origin: str = Field(..., example="MAA")
    destination: str = Field(..., example="DEL")
    date: str = Field(..., example="2026-07-20")


class SearchResponse(BaseModel):
    flights: List[Flight]


# ------------------------------------------------------------------
# RISK
# ------------------------------------------------------------------

"""
Pydantic models for TripSmart.
"""

from typing import List
from pydantic import BaseModel, Field


# ------------------------------------------------------------------
# Flight Model (Loaded from sample_data.json)
# ------------------------------------------------------------------

class Flight(BaseModel):
    flight_id: str
    airline: str
    flight_number: str

    departure_airport: str
    arrival_airport: str

    departure_time: str
    arrival_time: str

    duration_minutes: int

    stops: int
    layover_minutes: int

    fare: float

    status: str = "scheduled"


# ------------------------------------------------------------------
# SEARCH
# ------------------------------------------------------------------

class SearchRequest(BaseModel):
    origin: str = Field(..., example="MAA")
    destination: str = Field(..., example="DEL")
    date: str = Field(..., example="2026-07-20")


class SearchResponse(BaseModel):
    flights: List[Flight]


# ------------------------------------------------------------------
# RISK
# ------------------------------------------------------------------

class RiskBreakdown(BaseModel):

    stops_risk: float

    layover_risk: float

    late_departure_risk: float

    duration_risk: float

    cost_penalty: float

    comfort_score: float

    total_risk_score: float
    travel_rating: str

    reasons: list[str]


# ------------------------------------------------------------------
# RECOMMENDATION
# ------------------------------------------------------------------

class RankedFlight(BaseModel):
    flight: Flight
    risk: RiskBreakdown


class RecommendRequest(BaseModel):
    flights: List[Flight]


class RecommendResponse(BaseModel):
    best: RankedFlight
    alternatives: List[RankedFlight]
    explanation: str


# ------------------------------------------------------------------
# HEALTH
# ------------------------------------------------------------------

class HealthResponse(BaseModel):
    status: str


# ------------------------------------------------------------------
# RECOMMENDATION
# ------------------------------------------------------------------

class RankedFlight(BaseModel):
    flight: Flight
    risk: RiskBreakdown


class RecommendRequest(BaseModel):

    preference: str = "best"

    flights: List[Flight]


class RecommendResponse(BaseModel):

    recommended: RankedFlight

    best_overall: RankedFlight

    cheapest: RankedFlight

    fastest: RankedFlight

    lowest_risk: RankedFlight

    alternatives: List[RankedFlight]

    statistics: dict

    explanation: str


# ------------------------------------------------------------------
# HEALTH
# ------------------------------------------------------------------

class HealthResponse(BaseModel):
    status: str