from flask_caching import Cache

# Create a cache instance
cache = Cache(
    config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'tmp', 
        "CACHE_DEFAULT_TIMEOUT": 600
    }
)
def init_cache(server):
    cache.init_app(server)