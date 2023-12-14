-- List all Comedy shows in the Database.

SELECT s.title 
    FROM tv_shows AS s
    	INNER join tv_show_genres AS g
    	ON s.id = g.show_id
    
    	INNER JOIN tv_genres AS t
   	 ON t.id = g.genre_id
   	 WHERE g.name = "Comedy"
    ORDER BY s.title;
