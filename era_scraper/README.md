# README #

This is a scraper to get all open post research opportunities in [eracareers.pt](http://www.eracareers.pt/Search/index.aspx?task=search). The website sucks and a friend of mine needed to search opportunities more easily.

### How do I get set up? ###

* Install Scrapy (tested with version 0.24.6)
* Provide a file with proxies under `eracareers/middlewares/proxy.txt`
  * One proxy per line
  * Format: `http://username:password@host2:port`
  * You can also disable the proxy middleware in `settings.py` by commenting the following lines:
    * `'eracareers.middlewares.random_proxy.ProxyMiddleware': 100,`
    * `'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,`
* Install Elasticsearch and change the appropriate settings in `settings.py` or disable the pipeline
