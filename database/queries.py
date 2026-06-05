SEARCH_BY_KEYWORD = """
SELECT 
    film.title,
    film.release_year,
    film.rating,
    category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.title LIKE %s
ORDER BY film.title
LIMIT %s OFFSET %s;
"""

SEARCH_BY_GENRE = """
SELECT 
    film.title,
    film.release_year,
    film.rating,
    category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = %s
ORDER BY film.title
LIMIT %s OFFSET %s;
"""

COUNT_BY_GENRE = """
SELECT COUNT(*) AS total
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = %s;
"""

COUNT_BY_KEYWORD = """
SELECT COUNT(*) AS total
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.title LIKE %s;
"""

SEARCH_BY_GENRE_AND_YEAR = """
SELECT 
    film.title,
    film.release_year,
    film.rating,
    category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = %s
AND film.release_year BETWEEN %s AND %s
ORDER BY film.title
LIMIT %s OFFSET %s;
"""

COUNT_BY_GENRE_AND_YEAR = """
SELECT COUNT(*) AS total
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = %s
AND film.release_year BETWEEN %s AND %s;
"""

GET_ALL_GENRES = """
SELECT name
FROM category
ORDER BY name;
"""

GET_YEAR_RANGE = """
SELECT MIN(release_year) AS min_year, MAX(release_year) AS max_year
FROM film;
"""