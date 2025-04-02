from flask import Flask, request, jsonify
from backend.sql_connection import get_sql_connection
import json
import products_dao
import orders_dao
import uom_dao
import user_dao
import mysql.connector
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
try:
    connection = get_sql_connection()
    print("Database connected successfully")
except Exception as e:
    print(f"Database connection failed: {e}")
    connection = None

users = {}  

connection = get_sql_connection()
@app.route('/register', methods=['POST'])
def register():
    request_payload = request.get_json()  
    username = request_payload.get("username")  
    password = request_payload.get("password")  
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user_id = user_dao.register_user(connection, username, password)
    
    response = jsonify({
        "user_id": user_id,
        "message": "User registered successfully"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/login', methods=['POST'])
def login():
    request_payload = request.get_json()
    
    username = request_payload.get("username")
    password = request_payload.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    auth_response = user_dao.login_user(connection, username, password)

    if auth_response is None:
        return jsonify({"error": "Invalid username or password"}), 401  # Unauthorized

    return jsonify({
        "message": "Login successful",
        "token": auth_response["token"], 
        "user_id": auth_response["user_id"]
    }), 200


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
