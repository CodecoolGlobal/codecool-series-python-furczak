from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows(page=1):
    shows = data_manager.execute_select('''
        SELECT title, TO_CHAR(year,'YYYY') AS year, runtime,
        COALESCE(homepage, 'no url') AS homepage,
        COALESCE(trailer, 'no url') AS trailer, 
        ROUND(rating,1) AS rating, 
        STRING_AGG(genres.name, ', ') AS genre
        FROM shows 
        LEFT JOIN show_genres ON shows.id = show_genres.show_id
        LEFT JOIN genres ON genres.id = show_genres.genre_id
        GROUP BY shows.id
        ORDER BY shows.rating DESC 
        LIMIT 15 OFFSET ((%(page)s -1) * 15);
    ''', {'page': page})
    return shows


def get_page_number():
    return data_manager.execute_select('''
    SELECT COUNT(*) / 15 AS num FROM shows;
    ''', fetchall=False)
