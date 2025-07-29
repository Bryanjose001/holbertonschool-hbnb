document.addEventListener('DOMContentLoaded', () => {
    const placeId = getPlaceIdFromURL();
    const token = getCookie('authToken');

    if (!placeId) {
        alert('No place ID found in URL!');
        return;
    }

    fetchPlaceDetails(placeId, token);
    fetchReviews(placeId);
    setupReviewForm(placeId, token);

    if (!token) {
        document.getElementById('add-review').style.display = 'none';
    }
});

// Extract placeId from URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('placeId');
}

// Get JWT token from cookies
function getCookie(name) {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='));
    return cookieValue ? cookieValue.split('=')[1] : null;
}

// Fetch and display place details
async function fetchPlaceDetails(placeId, token) {
    try {
        const res = await fetch(`https://api.example.com/places/${placeId}`, {
            headers: token ? { 'Authorization': `Bearer ${token}` } : {}
        });

        if (!res.ok) throw new Error('Failed to fetch place details');

        const place = await res.json();
        const placeDetails = document.getElementById('places-list');
        placeDetails.innerHTML = `
            <div class="place-info">
                <h1>${place.name}</h1>
                <p><strong>Host:</strong> ${place.host}</p>
                <p><strong>Price:</strong> $${place.price}</p>
                <p><strong>Description:</strong> ${place.description}</p>
                <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
            </div>
        `;
    } catch (err) {
        console.error(err);
        alert('Error loading place details.');
    }
}

// Fetch and display reviews
async function fetchReviews(placeId) {
    try {
        const res = await fetch(`https://api.example.com/places/${placeId}/reviews`);
        if (!res.ok) throw new Error('Failed to fetch reviews');

        const reviews = await res.json();
        const reviewsSection = document.getElementById('reviews');
        reviewsSection.innerHTML = '<h2>Reviews</h2>';

        reviews.forEach(review => {
            const reviewDiv = document.createElement('div');
            reviewDiv.classList.add('review-card');
            reviewDiv.innerHTML = `
                <p><strong>Comment:</strong> ${review.comment}</p>
                <p><strong>User:</strong> ${review.user}</p>
                <p><strong>Rating:</strong> ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</p>
            `;
            reviewsSection.appendChild(reviewDiv);
        });
    } catch (err) {
        console.error(err);
    }
}

// Handle review form submission
function setupReviewForm(placeId, token) {
    const form = document.getElementById('review-form');
    const ratingSelect = document.getElementById('rating');

    // Populate rating dropdown
    for (let i = 1; i <= 5; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        ratingSelect.appendChild(option);
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const comment = document.getElementById('review-text').value;
        const rating = parseInt(document.getElementById('rating').value);

        try {
            const res = await fetch(`https://api.example.com/places/${placeId}/reviews`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({ comment, rating })
            });

            if (!res.ok) throw new Error('Failed to submit review');

            alert('Review submitted!');
            form.reset();
            fetchReviews(placeId); // Refresh reviews
        } catch (err) {
            console.error(err);
            alert('Error submitting review.');
        }
    });
}
