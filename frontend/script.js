let flights = [];

window.onload = () => {
  document.getElementById("date").value = new Date()
    .toISOString()
    .split("T")[0];
};

// ----------------------------
// Search Flights
// ----------------------------
async function searchFlights() {
  const body = {
    origin: document.getElementById("origin").value.toUpperCase(),
    destination: document.getElementById("destination").value.toUpperCase(),
    date: document.getElementById("date").value,
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const data = await response.json();

    flights = data.flights || [];

   

    const container = document.getElementById("flightList");

    if (flights.length === 0) {
      container.innerHTML = "<p>No matching flights found.</p>";

      return;
    }

    let html = "";

    flights.forEach((f) => {
      html += `
            <div class="flight-card">

                <h3>${f.airline}</h3>

                <p><strong>${f.flight_number}</strong></p>

                <p>${f.departure_airport} ➜ ${f.arrival_airport}</p>

                <p>Departure : ${f.departure_time}</p>

                <p>Arrival : ${f.arrival_time}</p>

                <p>Duration : ${f.duration_minutes} mins</p>

                <p>Stops : ${f.stops}</p>

                <p>Fare : ₹${f.fare}</p>

            </div>
            `;
    });

    html += `
        <br>
        <button onclick="recommend()">
            Get Recommendation
        </button>
        `;

    container.innerHTML = html;
  } catch (err) {
    console.error(err);

    alert("Unable to fetch flights.");
  }
}

// ----------------------------
// Recommend
// ----------------------------

async function recommend() {
  try {
    const response = await fetch("http://127.0.0.1:8000/recommend", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        preference: document.getElementById("preference").value,
        flights: flights,
      }),
    });

    const data = await response.json();

    const r = data.recommended;

    document.getElementById("recommendation").classList.remove("hidden");

    //------------------------------------------------
    // Main Recommendation Card
    //------------------------------------------------

    document.getElementById("recommendationCard").innerHTML = `

        <div class="flight-card recommended">

            <h3>${r.flight.airline}</h3>

            <h2>${r.flight.flight_number}</h2>

            <p><b>${r.flight.departure_airport}</b>
            ➜
            <b>${r.flight.arrival_airport}</b></p>

            <p>Fare : ₹${r.flight.fare}</p>

            <p>Duration : ${r.flight.duration_minutes} mins</p>

            <p>Stops : ${r.flight.stops}</p>

            <p>Risk Score :
                <strong>${r.risk.total_risk_score}</strong>
            </p>

            <p>Comfort :
                ${r.risk.comfort_score}/100
            </p>

            <p>Travel Rating :
                ${r.risk.travel_rating}
            </p>

        </div>

        `;

    //------------------------------------------------
    // Reasons
    //------------------------------------------------

    document.getElementById("reasonsList").innerHTML = r.risk.reasons
      .map((reason) => `<li>${reason}</li>`)
      .join("");

    //------------------------------------------------
    // Statistics
    //------------------------------------------------

    document.getElementById("statsBlock").innerHTML = `

        <p><b>Total Flights :</b>
        ${data.statistics.total_flights}</p>

        <p><b>Average Fare :</b>
        ₹${data.statistics.average_fare}</p>

        <p><b>Lowest Fare :</b>
        ₹${data.statistics.lowest_fare}</p>

        <p><b>Highest Fare :</b>
        ₹${data.statistics.highest_fare}</p>

        <p><b>Average Duration :</b>
        ${data.statistics.average_duration} mins</p>

        <p><b>Direct Flights :</b>
        ${data.statistics.direct_flights}</p>

        <p><b>Connecting Flights :</b>
        ${data.statistics.connecting_flights}</p>

        `;

    //------------------------------------------------
    // AI Explanation
    //------------------------------------------------

    document.getElementById("explanation").innerHTML = data.explanation;
  } catch (err) {
    console.error(err);

    alert("Unable to generate recommendation.");
  }
}
