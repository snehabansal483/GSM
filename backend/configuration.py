from functools import wraps
from flask import jsonify, request
import jwt

# Secret key for JWT (Keep it safe in an environment variable in production)
SECRET_KEY = "sdfdjghkgjljalkgkdmgdasfbhnsbvbdavmbd"



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        try:
            # Ensure token follows "Bearer <token>" format
            if "Bearer " in token:
                token = token.split("Bearer ")[1]

            # Decode JWT token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = data["user_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token!"}), 401

        return f(user_id, *args, **kwargs)

    return decorated
