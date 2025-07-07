CREATE TABLE User (
    id TEXT PRIMARY KEY, -- UUID stored as CHAR(36) format
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);
CREATE TABLE Place (
    id TEXT PRIMARY KEY, -- UUID stored as CHAR(36) format
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    owner_id TEXT NOT NULL, -- Foreign key to User table
    FOREIGN KEY (owner_id) REFERENCES User(id)
        --ON DELETE CASCADE, -- Delete places if user is deleted
        --ON UPDATE CASCADE -- Update places if user id is updated
);
CREATE TABLE Review (
    id TEXT PRIMARY KEY, -- UUID stored as CHAR(36) format
    text TEXT NOT NULL,
    rating REAL NOT NULL,
    place_id TEXT NOT NULL, -- Foreign key to Place table
    user_id TEXT NOT NULL, -- Foreign key to User table
    FOREIGN KEY (place_id) REFERENCES Place(id)
        --ON DELETE CASCADE, -- Delete reviews if place is deleted
        --ON UPDATE CASCADE, -- Update reviews if place id is updated
    FOREIGN KEY (user_id) REFERENCES User(id)
        --ON DELETE CASCADE, -- Delete reviews if user is deleted
        --ON UPDATE CASCADE -- Update reviews if user id is updated
);
CREATE TABLE Amenity (
    id TEXT PRIMARY KEY, -- UUID stored as CHAR(36) format
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE Place_Amenity (
    place_id TEXT NOT NULL, -- Foreign key to Place table
    amenity_id TEXT NOT NULL, -- Foreign key to Amenity table
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id)
        --ON DELETE CASCADE, -- Delete place-amenity link if place is deleted
        --ON UPDATE CASCADE, -- Update place-amenity link if place id is updated
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id)
        --ON DELETE CASCADE, -- Delete place-amenity link if amenity is deleted
        --ON UPDATE CASCADE -- Update place-amenity link if amenity id is updated
);

-- this are the tables creation scripts for the HBnB application
-- they define the structure of the database and relationships between entities
