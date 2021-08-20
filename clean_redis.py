import redis

r = redis.StrictRedis(host="localhost",port=6379,decode_responses=True)

