DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'testapp',
]

ROOT_URLCONF = 'testapp.urls'

SECRET_KEY = "shh...it's a seakret"

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6381',
        'OPTIONS': {
            'DB': 15,
            'PASSWORD': 'yadayada',
            'PARSER_CLASS': 'redis.connection._HiredisParser',
            'PICKLE_VERSION': 2,
            'CONNECTION_POOL_CLASS': 'redis.ConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 2,
            }
        },
    },
}

MIDDLEWARE_CLASSES = tuple()

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
