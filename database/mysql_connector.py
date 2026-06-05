import pymysql
import pymysql.cursors

from database.queries import SEARCH_BY_GENRE_AND_YEAR, SEARCH_BY_GENRE, SEARCH_BY_KEYWORD, COUNT_BY_GENRE_AND_YEAR, COUNT_BY_KEYWORD, COUNT_BY_GENRE, GET_ALL_GENRES, GET_YEAR_RANGE

class MySQLConnector:

    def __init__(self, hostname=None, username=None, password=None, port=3306, database=None, connection=None):
        
            self._hostname = hostname
            self._username = username
            self._password = password
            self._port = port
            self._database = database
            self._connection = connection

    def connect(self):
        self._connection = pymysql.connect(
            host = self._hostname,
            user = self._username,
            password = self._password,
            port = self._port,
            database = self._database,
            cursorclass = pymysql.cursors.DictCursor
        )

    def execute_select(self, query, params=None):
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result

    def close(self):
        if self._connection:
            self._connection.close()

    
    def search_by_keyword(self, keyword, limit=10, offset=0):
        params = (f'%{keyword}%', limit, offset)
        return self.execute_select(SEARCH_BY_KEYWORD, params)
    
    def search_by_genre(self, genre, limit=10, offset=0):
        return self.execute_select(SEARCH_BY_GENRE, (genre, limit, offset))

    def search_by_genre_and_year(self, genre, start_year, end_year, limit=10, offset=0):
        params = (genre, start_year, end_year, limit, offset)
        return self.execute_select(SEARCH_BY_GENRE_AND_YEAR, params)

    def count_by_keyword(self, keyword):
        result = self.execute_select(COUNT_BY_KEYWORD, (f"%{keyword}%",))
        return result[0]["total"]
    
    def count_by_genre(self, genre):
        result = self.execute_select(COUNT_BY_GENRE, (genre,))
        return result[0]["total"]
    
    def count_by_genre_and_year(self, genre, start_year, end_year):
        result = self.execute_select(
            COUNT_BY_GENRE_AND_YEAR,
            (genre, start_year, end_year)
            )
        return result[0]["total"]
    
    def get_all_genres(self):
        return self.execute_select(GET_ALL_GENRES)
    
    def get_years_range(self):
        return self.execute_select(GET_YEAR_RANGE)