from database.mysql_connector import MySQLConnector
from database.mysql_connector import run_mysql_connector

from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


if __name__ == "__main__":
    
    db = MySQLConnector(
    hostname = MYSQL_HOST,
    username = MYSQL_USER,
    password = MYSQL_PASSWORD,
    port = MYSQL_PORT,
    database = MYSQL_DATABASE
    )
        
    run_mysql_connector(db)