# QR Code & URL Shortener 🔗

A modern, user-friendly Flask web application for generating QR codes and shortening URLs with a beautiful, responsive interface.

## Features ✨

- **QR Code Generation**: Create QR codes from any text or URL
- **URL Shortening**: Generate short URLs with MD5 hash-based codes
- **Download QR Codes**: Download generated QR codes as PNG images
- **Copy to Clipboard**: Easily copy shortened URLs
- **Responsive Design**: Works perfectly on mobile and desktop
- **Modern UI**: Clean, gradient-based interface with smooth animations
- **Real-time Results**: Instant generation without page reloads

## Tech Stack 🛠️

- **Backend**: Flask (Python)
- **QR Generation**: qrcode library with Pillow
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with gradients and animations

## Installation 📦

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/rahit91890/qr-url-generator.git
cd qr-url-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage 📖

### Generate QR Code

1. Open the application
2. Enter any text or URL in the QR Code tab
3. Click "Generate QR Code"
4. Download the generated QR code image

### Shorten URL

1. Switch to the "Shorten URL" tab
2. Enter a long URL
3. Click "Shorten URL"
4. Copy the shortened URL to clipboard
5. Share the short URL (it redirects to the original)

## Project Structure 📁

```
qr-url-generator/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore            # Git ignore rules
│
└── templates/
    └── index.html        # Frontend HTML with embedded CSS/JS
```

## API Endpoints 🔌

### POST `/generate-qr`
Generate a QR code from text/URL

**Request:**
```json
{
  "text": "https://example.com"
}
```

**Response:**
```json
{
  "success": true,
  "image": "data:image/png;base64,..."
}
```

### POST `/shorten-url`
Shorten a URL

**Request:**
```json
{
  "url": "https://example.com/very-long-url"
}
```

**Response:**
```json
{
  "success": true,
  "short_url": "http://localhost:5000/s/abc123",
  "code": "abc123"
}
```

### GET `/s/<code>`
Redirect to original URL

## Deployment 🚀

### Local Deployment

The app runs on `0.0.0.0:5000` by default, making it accessible on your local network.

### Production Deployment Options

1. **Heroku**: Deploy using Gunicorn
2. **PythonAnywhere**: Simple Python web hosting
3. **Railway**: Modern deployment platform
4. **Render**: Free tier available
5. **DigitalOcean App Platform**: Managed hosting

### Production Configuration

For production, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

And use a production WSGI server like Gunicorn:
```bash
gunicorn app:app
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author 👤

**Rahit Biswas**
- GitHub: [@rahit91890](https://github.com/rahit91890)
- Website: [codaphics.com](https://codaphics.com)
- Email: r.codaphics@gmail.com

## Acknowledgments 🙏

- Flask framework for making web development easy
- qrcode library for QR code generation
- Open source community for inspiration

## Support 💬

If you found this project helpful, please give it a ⭐ on GitHub!

---

Made with ❤️ by Rahit Biswas
