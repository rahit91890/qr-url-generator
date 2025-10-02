from flask import Flask, render_template, request, jsonify, send_file
import qrcode
from io import BytesIO
import hashlib
import json
import os
from datetime import datetime

app = Flask(__name__)

# In-memory storage for URL mappings (for demo purposes)
url_database = {}

def generate_short_code(url):
    """Generate a short code using hash of URL and timestamp"""
    timestamp = str(datetime.now().timestamp())
    hash_input = url + timestamp
    short_hash = hashlib.md5(hash_input.encode()).hexdigest()[:6]
    return short_hash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to BytesIO
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Convert to base64 for sending to frontend
        import base64
        img_base64 = base64.b64encode(img_io.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{img_base64}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/shorten-url', methods=['POST'])
def shorten_url():
    try:
        data = request.json
        original_url = data.get('url', '')
        
        if not original_url:
            return jsonify({'error': 'No URL provided'}), 400
        
        # Check if URL already exists
        for code, url in url_database.items():
            if url == original_url:
                short_url = f"{request.host_url}s/{code}"
                return jsonify({
                    'success': True,
                    'short_url': short_url,
                    'code': code
                })
        
        # Generate new short code
        short_code = generate_short_code(original_url)
        url_database[short_code] = original_url
        
        short_url = f"{request.host_url}s/{short_code}"
        
        return jsonify({
            'success': True,
            'short_url': short_url,
            'code': short_code
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/s/<code>')
def redirect_short_url(code):
    """Redirect short URL to original URL"""
    original_url = url_database.get(code)
    if original_url:
        from flask import redirect
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
