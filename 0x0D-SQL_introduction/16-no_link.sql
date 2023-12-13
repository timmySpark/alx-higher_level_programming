-- Lists all records of the table second_table of the database 
-- Rows without a name value should nit be listed
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score

SELECT score, name 
FROM second_table
WHERE name is NOT NULL
ORDER BY score DESC;
