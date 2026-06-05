from database.mysql_connector import MySQLConnector

from utils.ui import buttons_menu
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def main():
    main_db = MySQLConnector(
        hostname = MYSQL_HOST,
        username = MYSQL_USER,
        password = MYSQL_PASSWORD,
        port = MYSQL_PORT,
        database = MYSQL_DATABASE
    )

    try:
        main_db.connect()
        buttons_menu(main_db)

    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return
    finally:
        main_db.close()

        
if __name__ == "__main__":
    main()
else:
    print("This module is not intended to be imported. Please run it directly.")