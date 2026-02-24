from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# CORS - Manual handling (most reliable method)
@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    
    # Allow your Vercel domain and localhost
    allowed = [
        'https://jan-sultan.vercel.app',
        'https://my-profile-tan-seven.vercel.app',
        'http://localhost:3000',
        'http://localhost:5173'
    ]
    
    if origin in allowed:
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
    
    return response

# Handle OPTIONS preflight requests
@app.route('/api/<path:path>', methods=['OPTIONS'])
def handle_options(path):
    response = jsonify({'status': 'ok'})
    origin = request.headers.get('Origin')
    allowed = [
        'https://jan-sultan.vercel.app',
        'https://my-profile-tan-seven.vercel.app',
        'http://localhost:3000',
        'http://localhost:5173'
    ]
    if origin in allowed:
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

# Supabase config
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

def supabase_request(method, table, data=None, params=None):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    if method == "GET":
        response = requests.get(url, headers=headers, params=params, timeout=10)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data, timeout=10)
    
    response.raise_for_status()
    return response.json()

@app.route('/api/guestbook', methods=['GET'])
def get_guestbook():
    try:
        params = {"order": "created_at.desc"}
        data = supabase_request("GET", "guestbook", params=params)
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/guestbook', methods=['POST'])
def post_guestbook():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not message:
            return jsonify({"success": False, "error": "Name and message required"}), 400
        
        entry = {"name": name[:40], "message": message[:280]}
        result = supabase_request("POST", "guestbook", data=entry)
        return jsonify({"success": True, "data": result[0]}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/contact', methods=['POST'])
def post_contact():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email or '@' not in email:
            return jsonify({"success": False, "error": "Valid name and email required"}), 400
        
        contact_data = {"name": name, "email": email, "message": message}
        result = supabase_request("POST", "contacts", data=contact_data)
        return jsonify({"success": True, "data": result[0]}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)