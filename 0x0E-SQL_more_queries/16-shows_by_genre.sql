-- Lists all shows, and all genres linked to that show,
--				from the database hbtn_0d_tvshows.

SELECT s.title, g.name
    FROM tv_shows AS s
        LEFT JOIN tv_show_genres as ts
        ON s.id = ts.show_id

        LEFT JOIN tv_genres as g
        ON g.id = ts.genre_id
    ORDER BY s.title;
