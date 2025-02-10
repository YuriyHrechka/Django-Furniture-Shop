from django.core.cache import cache


class CacheMixin(object):
    @staticmethod
    def set_get_cache(query, cache_name, cache_time):
        data = cache.get(cache_name)

        if not data:
            data = query
            cache.set(cache_name, data, cache_time)

        return data
