## Eracareers
This project is a lightweight alternative version of [eracareers.pt](http://www.eracareers.pt), or more specifically the ["research opportunity" search section](http://www.eracareers.pt/Search/index.aspx?task=search). A friend of mine was frustrated with it and asked if I could do something about it. So I did.

The original [eracareers.pt](http://www.eracareers.pt) is "co-funded by the European Commission and maintained by the Portuguese Foundation for Science and Technology". Although it's supposed to be replaced with a better version as [mentioned here](http://www.euraxess.pt), it seems to be taking a while.

The project consists of 3 main components:
* A scraper to get all the data - [Scrapy](http://scrapy.org/)
* A search engine to search all the data - [Elasticsearch](https://www.elastic.co/)
* A frontend to present all the data - [Python](https://www.python.org/) + [Flask](http://flask.pocoo.org/)

Note: this is still work in progress!

## Installation

* Clone this repo
* Install Scrapy 1.0 - check their [excellent documentation](http://scrapy.readthedocs.org/en/latest/) to see how
* Install Elasticsearch - [download here](https://www.elastic.co/downloads/elasticsearch)
* Install Flask and pyes - use `pip install flask` and `pip install pyes`
* Provide a file with proxies named `proxies.txt` in `era_scraper/eracareers/middlewares` (or disable the 2 proxy middlewares in `era_scraper/eracareers/settings.py` if you don't have one)

## Usage

* Start up your elasticsearch instance
* Run the scraper to get the latest data - in the folder `era_scraper` do `scrapy crawl era`
* Start up the app - in the folder `era_search` do `python run.py`

This is enough to get it up and running locally (it's using Flask's development server). For a more robust installation you should probably run the app behind a webserver like nginx.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## History

History is being written as we speak.

## Credits

* Many thanks to Michael Malocha for the [Scrapy Elasticsearch Pipeline](https://github.com/knockrentals/scrapy-elasticsearch)
* Many thank to [svola](https://github.com/svola) for the Flask template ([fantasticsearch](https://github.com/svola/fantasticsearch)) to integrate with Elasticsearch which I shamelessly borrowed and modified

## License

Copyright 2015 André Bergonse

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
