from flask import Flask
import redis
import os
app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)


@app.route('/')
def hello_world():
    return 'We are running our first container - from CoderCo'


@app.route('/count')
def count():
    try:
        visits = redis_client.get("visits")

        if visits is None:
            redis_client.set("visits", 1)
            visits = 1
        else:
            visits = redis_client.incr("visits")

        return f"Visit count: {visits}"
    except redis.exceptions.RedisError:
        return "Redis connection error."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)