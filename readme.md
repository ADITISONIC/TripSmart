# ✈️ TripSmart – AI-Assisted Flight Recommendation System

TripSmart is a **FastAPI-based intelligent flight recommendation system** that helps travelers choose the best itinerary instead of simply selecting the cheapest flight.

The application analyzes flights using a rule-based recommendation engine that evaluates:

- 💰 Ticket Fare
- ⏱ Travel Duration
- 🛫 Number of Stops
- ⏳ Layover Time
- 🌙 Departure Timing
- 😊 Comfort Score
- ⚠ Travel Risk

Based on these factors, TripSmart recommends the **Best Overall**, **Cheapest**, **Fastest**, and **Lowest Risk** flight while providing an AI-style explanation of the recommendation.

---

# 🚀 Features

### 🔍 Flight Search

Search flights using:

- Origin Airport
- Destination Airport
- Travel Date

The backend filters and returns only matching flights.

---

### 📊 Flight Risk Analysis

Each flight is evaluated using an explainable rule-based scoring engine.

Risk factors include:

- Number of stops
- Tight layovers
- Overnight departures
- Long journey duration
- Ticket price

Every recommendation is transparent and includes the reasons behind the score.

---

### 🤖 Intelligent Recommendation Engine

TripSmart generates multiple recommendations:

- ⭐ Best Overall
- 💸 Cheapest Flight
- ⚡ Fastest Flight
- 🛡 Lowest Risk Flight

The overall recommendation considers a balanced combination of:

- Travel risk
- Duration
- Fare
- Comfort

instead of simply choosing the cheapest ticket.

---

### 📈 Search Statistics

The application also displays:

- Total flights found
- Average fare
- Cheapest fare
- Highest fare
- Average journey duration
- Number of direct flights
- Number of connecting flights

---

### 🧠 AI-style Recommendation Summary

Instead of returning only numbers, TripSmart generates a human-readable explanation describing why a particular flight is recommended.

Example:

> We recommend IndiGo 6E452 because it offers the best balance between travel time, reliability and cost. It is the fastest direct flight with the lowest overall risk score while remaining competitively priced.

---

### ✅ Unit Tested

The recommendation engine and risk scoring logic are fully unit tested using **PyTest**.

Tests cover:

- Risk calculation
- Flight ranking
- Recommendation logic
- Edge cases

---

# 🏗 Project Architecture

```
TripSmart
│
├── backend
│   ├── app.py
│   ├── models.py
│   ├── recommender.py
│   ├── risk_engine.py
│   ├── ai_summary.py
│   └── sample_data.json
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests
│   ├── test_risk.py
│   └── test_recommendation.py
│
├── requirements.txt
├── README.md
└── pytest.ini
```

---

# ⚙ Tech Stack

### Backend

- Python
- FastAPI
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript

### Testing

- PyTest

### Version Control

- Git
- GitHub

---

# 🧮 Recommendation Algorithm

Each itinerary is evaluated using multiple factors.

## Risk Score

Risk increases with:

- Multiple stops
- Tight layovers
- Long journeys
- Late-night departures

## Comfort Score

Comfort increases for:

- Direct flights
- Daytime departures
- Short travel duration

## Overall Recommendation

The best flight is selected using a weighted score combining:

- Travel Risk
- Journey Duration
- Ticket Fare

instead of relying on only one metric.

---

# 📡 API Endpoints

## Search Flights

```
POST /search
```

Example Request

```json
{
  "origin": "MAA",
  "destination": "DEL",
  "date": "2026-07-17"
}
```

---

## Get Recommendation

```
POST /recommend
```

Returns

- Best Overall Flight
- Cheapest Flight
- Fastest Flight
- Lowest Risk Flight
- Alternative Flights
- Statistics
- AI Recommendation Summary

---

## Health Check

```
GET /health
```

---

# ▶ Running the Project

## Clone Repository

```bash
git clone https://github.com/yourusername/TripSmart.git

cd TripSmart
```

---

## Create Virtual Environment

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn backend.app:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

Using VS Code Live Server

or

```bash
python -m http.server 5500
```

Open

```
http://localhost:5500/frontend
```

---

# 🧪 Run Unit Tests

```bash
pytest
```

Example Output

```
==================
7 passed
==================
```

---

# 🎯 Future Improvements

- Live Flight API Integration
- Airport Autocomplete
- Flight Delay Prediction
- Weather-aware Recommendations
- Price Trend Prediction
- User Authentication
- Flight Bookmarking
- Responsive Mobile UI

---

# 💡 Learning Outcomes

This project demonstrates:

- REST API Development
- Backend System Design
- Rule-Based Recommendation Systems
- Explainable AI Concepts
- Unit Testing
- Modular Software Architecture
- Clean Code Practices
- Frontend & Backend Integration

---

