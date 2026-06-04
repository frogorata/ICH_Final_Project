SEARCH_BY_KEYWORD = """
SELECT title, release_year
FROM film
WHERE title LIKE %s
LIMIT %s OFFSET %s;
"""

