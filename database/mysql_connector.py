import pymysql
import pymysql.cursors

from database.queries import SEARCH_BY_KEYWORD

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

def run_mysql_connector(db: MySQLConnector):

        try:
            db.connect()    
            print(f"Connecting to MySQL database at {db._hostname} with username {db._username}")

            keyword = "Inter"  # test keyword for searching
            params = (f'%{keyword}%', 10, 0)  # Example parameters for the query (keyword, limit, offset)
            movies = db.execute_select(SEARCH_BY_KEYWORD, params)  # Example query with parameters

            print("Movies from the database:")
            for movie in movies:
                print(f"{movie['title']} ({movie['release_year']})")

        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            return None
        finally:
             db.close()