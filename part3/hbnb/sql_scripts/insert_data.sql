INSERT INTO User (id, first_name, last_name, email, password, is_admin) VALUES
('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'Admin', 'HBnB', 'admin@hbnb.io', '$2b$12$zROEObVln5urtrUZiTY2Me8e6cZ5GzZJk1K5Tp58Uvq1h6vNRh/qe', 1);

-- Create the Amenity table
CREATE TABLE Amenity (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Insert initial amenities with UUIDv4 values
INSERT INTO Amenity (id, name) VALUES
('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'WiFi'),
('9b2c13f2-7e4a-4b48-bcbc-0ad3c6aa27c4', 'Swimming Pool'),
('0f8fad5b-d9cb-469f-a165-70867728950e', 'Air Conditioning');