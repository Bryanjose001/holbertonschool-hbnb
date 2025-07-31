const db = require('../db');

async function addReview(placeId, userId, comment, rating) {
    const query = `
        INSERT INTO reviews (place_id, user_id, comment, rating)
        VALUES ($1, $2, $3, $4)
        RETURNING *;
    `;
    const values = [placeId, userId, comment, rating];
    const result = await db.query(query, values);
    return result.rows[0];
}

module.exports = {
    addReview
};
