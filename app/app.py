from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv("APP_MESSAGE", "Default Message")
    return message

@app.route('/health')
def health():
    return {
        "status": "UP"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)