import datetime
import jwt
import mysql.connector
from backend.sql_connection import get_sql_connection
import hashlib

SECRET_KEY = "sdfdjghkgjljalkgkdmgdasfbhnsbvbdavmbd"

def register_user(connection, username, password):
    cursor = connection.cursor()

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    data = (username, hashed_password)

    try:
        cursor.execute(query, data)
        connection.commit()
        return cursor.lastrowid  
    except mysql.connector.IntegrityError:
        return None  


def login_user(connection, username, password):
    cursor = connection.cursor(dictionary=True)  # Fetch results as dictionary

    # Hash the entered password to compare with stored hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    query = "SELECT user_id FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, hashed_password))
    user = cursor.fetchone()  # Fetch user data

    if user:  # If user exists, generate token
        user_id = user["user_id"]
        
        # Generate JWT token with expiration time
        token_payload = {
            "user_id": user_id,
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # Token expires in 2 hours
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")

        return {
            "message": "Login successful",
            "token": token,  
            "user_id": user_id
        }
    else:
        return None 
 
