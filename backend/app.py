"""
app.py

TripSmart API

Flow

User
   │
   ▼
POST /search
   │
Loads sample_data.json
Filters by origin & destination
Returns matching flights
   │
   ▼
POST /recommend
   │
Scores flights
Ranks them
Generates explanation
Returns recommendation
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.models import (
    Flight,
    SearchRequest,
    SearchResponse,
    RecommendRequest,
    RecommendResponse,
    HealthResponse,
)

from backend.data_loader import search_flights
from backend.recommender import recommend


app = FastAPI(
    title="TripSmart API",
    version="1.0.0",
    description="AI-powered Flight Recommendation Engine",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------------
# Home
# --------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Welcome to TripSmart API"
    }


# --------------------------------------------------------
# Health Check
# --------------------------------------------------------

@app.get(
    "/health",
    response_model=HealthResponse,
)
def health():

    return HealthResponse(
        status="Healthy"
    )


# --------------------------------------------------------
# Search Flights
# --------------------------------------------------------

@app.post(
    "/search",
    response_model=SearchResponse,
)
def search(request: SearchRequest):

    flights = search_flights(
        origin=request.origin,
        destination=request.destination,
    )

    if not flights:
        raise HTTPException(
            status_code=404,
            detail="No flights found for this route."
        )

    return SearchResponse(
        flights=flights
    )


# --------------------------------------------------------
# Recommend Best Flight
# --------------------------------------------------------

@app.post(
    "/recommend",
    response_model=RecommendResponse,
)
def recommend_flight(request: RecommendRequest):

    if len(request.flights) == 0:

        raise HTTPException(
            status_code=400,
            detail="Flight list is empty."
        )

    return recommend(request.flights)