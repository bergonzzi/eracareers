import random
import logging

logger = logging.getLogger(__name__)


class ProxyMiddleware(object):
    def __init__(self, settings):
        proxy_file = settings.get('PROXY_LIST')
        self.proxies = open(proxy_file).read().splitlines()
        logger.info('Initializing with %s proxies', len(self.proxies))

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        proxy = random.choice(self.proxies)
        request.meta['proxy'] = proxy
        # logger.info('Using proxy %s for %s, %d proxies left', proxy, request.url, len(self.proxies))

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']

        logger.warning('Removing failed proxy <%s>, %d proxies left', proxy, len(self.proxies) - 1)

        try:
            self.proxies.remove(proxy)
        except ValueError:  # Proxy already removed by another request
            pass
