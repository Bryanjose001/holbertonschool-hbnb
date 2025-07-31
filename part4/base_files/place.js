document.addEventListener('DOMContentLoaded', async () => {
    const queryParams = new URLSearchParams(window.location.search);
    const placeId = queryParams.get('place_id');

    // Helper to get JWT token from cookies
    function getToken() {
        const cookieMatch = document.cookie.match('(^|;)\\s*token\\s*=\\s*([^;]+)');
        return cookieMatch ? cookieMatch.pop() : null;
    }

    const token = getToken();
    const isAuthenticated = !!token;

    const placeDetailsSection = document.getElementById('places-list');
    const reviewsSection = document.getElementById('reviews');
    const addReviewSection = document.getElementById('add-review');

    if (!placeId) {
        placeDetailsSection.innerHTML = '<p>Error: No place ID provided in URL.</p>';
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            headers: token ? {
                'Authorization': `Bearer ${token}`
            } : {}
        });

        if (!response.ok) {
            throw new Error('Failed to fetch place details');
        }

        const place = await response.json();

        // Populate place details
        const placeHTML = `
            <div class="place-info">
                <h1>name:${place.title}</h1>
                <p><strong>Price:</strong> $${place.price}</p>
                <p><strong>Description:</strong> ${place.description}</p>
                <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
            </div>
        `;
        placeDetailsSection.innerHTML = placeHTML;

        // Populate reviews
        /*const reviewCards = place.reviews.map(review => `
            <div class="review-card">
                <p><strong>Comment:</strong> ${review.comment}</p>
                <p><strong>User:</strong> ${review.user}</p>
                <p><strong>Rating:</strong> ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</p>
            </div>
        `).join('');
        reviewsSection.innerHTML += reviewCards;
*/
    } catch (error) {
        console.error(error);
        placeDetailsSection.innerHTML = `<p>Error loading place: ${error.message}</p>`;
    }

    // Toggle review form visibility
    addReviewSection.style.display = isAuthenticated ? 'block' : 'none';

    // Populate rating dropdown
    const ratingSelect = document.getElementById('rating');
    for (let i = 1; i <= 5; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        ratingSelect.appendChild(option);
    }

    // Handle review form submission
    const reviewForm = document.getElementById('review-form');
    reviewForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const reviewText = document.getElementById('review-text').value;
        const rating = parseInt(document.getElementById('rating').value);

        try {
            const res = await fetch(`https://your-api.com/api/places/${placeId}/reviews`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    comment: reviewText,
                    rating: rating
                })
            });

            if (!res.ok) {
                throw new Error('Failed to submit review');
            }

            alert('Review submitted!');
            location.reload();
        } catch (error) {
            alert('Error submitting review: ' + error.message);
        }
    });
});

// routes/places.js
const express = require('express');
const router = express.Router();
const db = require('../db'); // your database connection
const authMiddleware = require('../middleware/auth');

router.post('/api/v1/places/:placeId/reviews', authMiddleware, async (req, res) => {
    const { placeId } = req.params;
    const { comment, rating } = req.body;
    const userId = req.user.id;

    try {
        const insertReviewQuery = `
            INSERT INTO reviews (place_id, user_id, comment, rating)
            VALUES ($1, $2, $3, $4)
            RETURNING *;
        `;

        const result = await db.query(insertReviewQuery, [
            placeId,
            userId,
            comment,
            rating
        ]);

        res.status(201).json(result.rows[0]);
    } catch (err) {
        console.error('Error inserting review:', err);
        res.status(500).json({ message: 'Internal server error' });
    }
});

module.exports = router;

const express = require('express');
const Router = express.Router();
const authMiddleware = require('../middleware/auth');
const reviewModel = require('../models/reviewModel');

router.post('/api/v1/places/:placeId/reviews', authMiddleware, async (req, res) => {
    const { placeId } = req.params;
    const { comment, rating } = req.body;
    const userId = req.user.id;

    try {
        const review = await reviewModel.addReview(placeId, userId, comment, rating);
        res.status(201).json(review);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Could not add review' });
    }
});

module.exports = router;

const reviewsSection = document.getElementById('reviews');

// Clear old reviews (just in case)
reviewsSection.innerHTML = '<h2>Reviews</h2>';

if (place.reviews && place.reviews.length > 0) {
    place.reviews.forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';
        reviewCard.innerHTML = `
            <p><strong>Comment:</strong> ${review.comment}</p>
            <p><strong>User:</strong> ${review.user}</p>
            <p><strong>Rating:</strong> ${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</p>
        `;
        reviewsSection.appendChild(reviewCard);
    });
} else {
    const noReview = document.createElement('p');
    noReview.textContent = 'No reviews yet.';
    reviewsSection.appendChild(noReview);
}
const response = await fetch('mock-place.json');
const place = await response.json();
