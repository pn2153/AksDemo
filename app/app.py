from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Read message from ConfigMap env variable
message = os.getenv("APP_MESSAGE", "Default Message")

# MongoDB connection string
MONGO_URL = os.getenv("MONGO_URL")

@app.route('/')
def home():
    return message

@app.route('/health')
def health():
    return {
        "status": "UP"
    }

@app.route('/dbcheck')
def dbcheck():
    try:
        client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)

        # ping database
        client.admin.command('ping')

        return {
            "mongodb": "Connected successfully"
        }

    except Exception as e:
        return {
            "mongodb": "Connection failed",
            "error": str(e)
        }, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)