-- Create a table id_not_null with an id of 1 by Default.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL
	);
