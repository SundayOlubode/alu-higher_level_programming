-- 10-genre_id_by_show.sql

curl 'https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql' -s

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
