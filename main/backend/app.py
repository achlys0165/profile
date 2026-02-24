from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

# CORS
CORS(app, origins=[
    os.environ.get("FRONTEND_URL", "http://localhost:3000"),
    "http://localhost:5173"
])

# Supabase REST API config
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

def supabase_request(method, table, data=None, params=None):
    """Make request to Supabase REST API"""
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    if method == "GET":
        response = requests.get(url, headers=headers, params=params)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    else:
        raise ValueError(f"Unsupported method: {method}")
    
    response.raise_for_status()
    return response.json()

# ============ GUESTBOOK ============

@app.route('/api/guestbook', methods=['GET'])
def get_guestbook():
    """Get all guestbook entries, newest first"""
    try:
        params = {
            "order": "created_at.desc"
        }
        data = supabase_request("GET", "guestbook", params=params)
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/guestbook', methods=['POST'])
def post_guestbook():
    """Create new guestbook entry"""
    try:
        data = request.get_json()
        
        # Validation
        name = data.get('name', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not message:
            return jsonify({"success": False, "error": "Name and message required"}), 400
        
        if len(name) > 40 or len(message) > 280:
            return jsonify({"success": False, "error": "Field too long"}), 400
        
        entry = {
            "name": name,
            "message": message
        }
        
        result = supabase_request("POST", "guestbook", data=entry)
        return jsonify({"success": True, "data": result[0]}), 201
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# ============ CONTACT ============

@app.route('/api/contact', methods=['POST'])
def post_contact():
    """Create new contact message"""
    try:
        data = request.get_json()
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email:
            return jsonify({"success": False, "error": "Name and email required"}), 400
        
        if '@' not in email:
            return jsonify({"success": False, "error": "Invalid email"}), 400
        
        contact_data = {
            "name": name,
            "email": email,
            "message": message
        }
        
        result = supabase_request("POST", "contacts", data=contact_data)
        return jsonify({"success": True, "data": result[0]}), 201
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# ============ HEALTH ============

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)