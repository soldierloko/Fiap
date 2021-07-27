import redis

redis_host = 'fiap.1qdfgg.ng.0001.use2.cache.amazonaws.com'
redis_port = 6379


def redis_string():
    try:
        r = redis.StrictRedis(host=redis_host,port=redis_port, decode_responses=True)
        r.set('Message', "Hello Word!")
        msg = r.get('Message')
        print(msg)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    redis_string()