# import mysql.connector
# __cnx = None
# def get_sql_connection():
#     global __cnx
#     if __cnx is None:
#         __cnx = mysql.connector.connect(user='root', password='Sneha@28',
#                                     host='127.0.0.1',
#                                     database='grocery_store')
    
#     return __cnx

import mysql.connector
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Extract details from DATABASE_URL
database_url = os.getenv("DATABASE_URL")
if database_url:
    parsed_url = urlparse(database_url)
    db_host = parsed_url.hostname
    db_port = parsed_url.port
    db_user = parsed_url.username
    db_password = parsed_url.password
    db_name = parsed_url.path[1:]  # Skip the leading slash in the database name

    print(f"Connected to {db_name} on {db_host}:{db_port} as {db_user}")  # For debugging
else:
    print("DATABASE_URL is not set in the environment file.")

def get_sql_connection():
    return mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )

