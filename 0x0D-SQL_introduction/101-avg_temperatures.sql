-- Displays average temperature by city ordered by temperature

USE hbtn_0c_0
SELECT city, AVG(value) avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC ; 
