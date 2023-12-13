-- Create a table unique_id with an id of 1 by Default and Unique.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256) NOT NULL
	);
