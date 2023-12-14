-- Lists all shows contained in hbtn_0d_tvshows that have 
-- 						at least one genre linked.

SELECT m.name genre, 
	COUNT(*) number_of_shows
  FROM tv_genres AS m
        INNER JOIN tv_show_genres AS g
	ON m.id = g.genre_id
  GROUP BY m.name
  ORDER BY number_of_shows DESC;
