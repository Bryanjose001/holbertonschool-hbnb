-- places table
CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name TEXT,
    host TEXT,
    price NUMERIC,
    description TEXT,
    amenities TEXT[]
);

-- users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    email TEXT
);

-- reviews table
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    place_id INTEGER REFERENCES places(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    comment TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5)
);
