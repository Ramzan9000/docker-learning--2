from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    return "Welcome to my Flask + Redis App!"

@app.route('/count')
def count():
    count = cache.incr('visits')
    return f"Visit count: {count}"