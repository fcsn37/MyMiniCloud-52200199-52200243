from flask import Flask, jsonify, request # type: ignore
import time, requests, os
from jose import jwt # type: ignore
import json

ISSUER = os.getenv("OIDC_ISSUER", "http://authentication-identity-server:8080/realms/master")
AUDIENCE = os.getenv("OIDC_AUDIENCE", "myapp")
JWKS_URL = f"{ISSUER}/protocol/openid-connect/certs"
JWKS = None; TS = 0

def get_jwks():
    global JWKS, TS
    now = time.time()
    if not JWKS or now - TS > 600:
        JWKS = requests.get(JWKS_URL, timeout=5).json()
        TS = now
    return JWKS

app = Flask(__name__)

def load_students():
    # Tìm file students.json trong cùng thư mục
    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
            return data.get("students", []) 
    except FileNotFoundError:
        return []

# Endpoint: /student
@app.route('/student', methods=['GET'])
def get_students():
    students = load_students()
    return jsonify({
        "status": "success",
        "count": len(students),
        "data": students
    })

@app.get("/hello")
def hello(): return jsonify(message="Hello from App Server!")

@app.get("/secure")
def secure():
    auth = request.headers.get("Authorization","")
    if not auth.startswith("Bearer "):
        return jsonify(error="Missing Bearer token"), 401

    token = auth.split(" ",1)[1]
    try:
        payload = jwt.decode(token, get_jwks(), algorithms=["RS256"], audience=AUDIENCE, issuer=ISSUER)
        return jsonify(message="Secure resource OK",
                       preferred_username=payload.get("preferred_username"))
    except Exception as e:
        return jsonify(error=str(e)), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
