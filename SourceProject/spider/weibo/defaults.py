import redis

# For standalone use.
DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

PIPELINE_KEY = '%(spider)s:items'

REDIS_CLS = redis.StrictRedis

# Sane connection defaults.
REDIS_PARAMS = {
    #'socket_timeout': 30,
    #'socket_connect_timeout': 30,
    #'retry_on_timeout': True,
    'encoding': 'utf-8',
    #'url': 'http://rs:6379',
    'url':'http://localhost:6379'
}

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

START_URLS_KEY = '%(name)s:start_urls'
START_URLS_AS_SET = False
