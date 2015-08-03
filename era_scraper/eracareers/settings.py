# -*- coding: utf-8 -*-

import logging

BOT_NAME = 'eracareers'

SPIDER_MODULES = ['eracareers.spiders']
NEWSPIDER_MODULE = 'eracareers.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 50,
    'eracareers.middlewares.random_proxy.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'eracareers.middlewares.random_useragent.RandomUserAgentMiddleware': 400,
}

# Custom exporter to enforce field order
FEED_EXPORTERS = {
    'csv': 'eracareers.middlewares.csv_exporter.MyCsvItemExporter'
}

ITEM_PIPELINES = {
    # 'eracareers.pipelines.DuplicatesPipeline': 100,
    'eracareers.middlewares.elasticsearch.ElasticSearchPipeline': 200
}

ELASTICSEARCH_SERVER = 'localhost'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_USERNAME = ''
ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'eracareers'
ELASTICSEARCH_TYPE = 'job'
ELASTICSEARCH_UNIQ_KEY = 'id'
ELASTICSEARCH_LOG_LEVEL = logging.INFO
ELASTICSEARCH_MAPPING = 'eracareers/mapping.json'

FIELDS_TO_EXPORT = [
    'ref',
    'job',
    'summary',
    'main_field',
    'sub_field',
    'vacancies',
    'contract',
    'country',
    'city',
    'institute',
    'deadline',
    'org_name',
    'email',
    'website',
    'id',
    'url'
]

RETRY_TIMES = 4
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]
COOKIES_ENABLED = False

HTTPCACHE_ENABLED = True
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.LeveldbCacheStorage'
PROXY_LIST = 'eracareers/middlewares/proxies.txt'
