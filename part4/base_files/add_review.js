// Utility: Get JWT token from cookies
function getCookie(name) {
        const match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
        return match ? match[2] : null;
}

    const token = getCookie("authToken");
if (!token) {
    window.location.href = 'index.html';
}

// Extract placeId from URL
const urlParams = new URLSearchParams(window.location.search);
const placeId = urlParams.get('place_id');
if (!placeId) {
    alert('Missing place ID in URL.');
    window.location.href = 'index.html';
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('review-form');
    const reviewInput = document.getElementById('review');
    const ratingSelect = document.getElementById('rating');

    // Populate rating options (1-5)
    for (let i = 1; i <= 5; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = `${i} Star${i > 1 ? 's' : ''}`;
        ratingSelect.appendChild(option);
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const reviewText = reviewInput.value.trim();
        const rating = ratingSelect.value;

        console.log('reviewtext:',reviewText);
        console.log('rating:', rating);

            
        if (!reviewText || !rating) {
            alert('Please complete all fields.');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    place_id: placeId,
                    text: reviewText,
                    rating: Number(rating)
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || 'Error submitting review.');
            }

            alert('Review submitted successfully!');
            form.reset();
        } catch (error) {
            console.error('Submission failed:', error);
            alert('Failed to submit review: ' + error.message);
        }
    });
});
