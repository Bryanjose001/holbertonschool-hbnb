/* 
This is a SAMPLE FILE to get you started.
Please, follow the project instructions to complete the tasks.
*/

/*document.addEventListener('DOMContentLoaded', () => {
  DO SOMETHING 
  });*/

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const errorMessage = document.getElementById("error-message");
  const loginLink = document.getElementById("login-link");
  const placeDetailsSection = document.getElementById("place-details");
// Check if the user is already logged in
  const token = getCookie("authToken");

  if (token) {
    if (loginLink) loginLink.style.display = "none";
  } else {
    if (loginLink) loginLink.style.display = "block";
  }
// Fetch and display places if the section exists
  if (placeDetailsSection) {
    fetchPlaces();
  }
// Handle login form submission
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      errorMessage.textContent = "Error";

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
// Validate email and password
      try {
        const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ email, password })
        });

        if (!response.ok) {
          const errorData = await response.json();
          errorMessage.textContent = errorData.message || "Invalid credentials";
          return;
        }

        const data = await response.json();

        document.cookie = `authToken=${data.access_token}; path=/; max-age=${7 * 24 * 60 * 60}; SameSite=Strict; Secure`;
        window.location.href = "index.html";

      } catch (error) {
        console.error("Login error:", error);
        errorMessage.textContent = "Something went wrong. Please try again.";
      }
    });
  }
});
// Fetch places from the API and display them
async function fetchPlaces() {
  try {
    const token = getCookie("authToken");

    const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
      headers: token
        ? {
            "Authorization": `Bearer ${token}`,
          }
        : {},
    });

    if (!response.ok) throw new Error("Failed to fetch places");

    const places = await response.json();
    displayPlaces(places);
  } catch (error) {
    console.error("Error fetching places:", error);
  }
}

// Get a cookie by name
function getCookie(name) {
  const match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  return match ? match[2] : null;
}
function displayPlaces(places) {
  const placesListSection = document.getElementById("places-list");
  if (!placesListSection) return;

  placesListSection.innerHTML = ""; // Clear previous content

  places.forEach(place => {
    // Create container for the place
    const placeDiv = document.createElement("div");
    placeDiv.className = "place-info"; // Keeps your CSS class

    // Build the content using innerHTML
    placeDiv.innerHTML = `
      <h1>${place.name}</h1>
      <p><strong>Host:</strong> ${place.host}</p>
      <p><strong>Price:</strong> $${place.price}</p>
      <p><strong>Description:</strong> ${place.description}</p>
      <p><strong>Amenities:</strong> ${place.amenities.join(", ")}</p>
    `;

    // Append to the DOM
    placesListSection.appendChild(placeDiv);
  });
}

// Add this function to handle the login link visibility
// Simulate user authentication (later you will replace this with actual logic)
const isLoggedIn = checkAuthentication(); // Change to true to simulate a logged-in user

document.addEventListener("DOMContentLoaded", () => {
    const addReviewSection = document.getElementById("add-review");

    if (!isLoggedIn && addReviewSection) {
        addReviewSection.classList.add("hidden");
    }
     // Run authentication check
    checkAuthentication();
});
function checkAuthentication() {
    const token = getCookie('authToken');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        // Fetch places data if the user is authenticated
        fetchPlaces(token);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const priceFilter = document.getElementById('price-filter');

    // Step 1: Populate dropdown
    const priceOptions = [10, 50, 100, 'All'];
    priceOptions.forEach(price => {
        const option = document.createElement('option');
        option.value = price;
        option.textContent = price === 'All' ? 'All' : `$${price}`;
        priceFilter.appendChild(option);
    });

    // Step 2: Add event listener
    priceFilter.addEventListener('change', (event) => {
        const selected = event.target.value;
        const maxPrice = selected === 'All' ? Infinity : parseFloat(selected);
        const placeCards = document.querySelectorAll('.place-card');

        placeCards.forEach(card => {
            const priceText = card.querySelector('p').textContent;
            const match = priceText.match(/\$(\d+)/);
            const placePrice = match ? parseFloat(match[1]) : 0;

            if (placePrice <= maxPrice) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
  const API_ENDPOINT = "https://your-api.com/api/places"; // Replace with your actual endpoint

  // Function to retrieve JWT token
  function getJWTToken() {
    return localStorage.getItem("authToken"); // Adjust if stored elsewhere
  }

  // Function to fetch places from API
  async function fetchPlaces() {
    try {
      const token = getJWTToken();

      const response = await fetch(API_ENDPOINT, {
        method: "GET",
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const places = await response.json();
      displayPlaces(places);
    } catch (error) {
      console.error("Error fetching places:", error);
      const section = document.getElementById("places-list");
      if (section) section.innerHTML = "<p>Failed to load places.</p>";
    }
  }

  // Call the fetch function on load
  fetchPlaces();
});
