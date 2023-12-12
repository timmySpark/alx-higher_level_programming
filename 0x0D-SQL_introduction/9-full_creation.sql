-- Creates a tables secone_table and store values in the current database.
CREATE TABLE IF NOT EXISTS second_table(
	id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	score INT
	);
INSERT INTO second_table(id, name, score)
VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
