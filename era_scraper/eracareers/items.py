# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, MapCompose, Join


def remove_comments(x):
    return re.sub(r'<!--.*?-->', '', x)


def translate_date(x):
    # 28 August 2015
    # 27 Julho 2015
    # 31 Dezembro 2015

    date_map = {
        'Janeiro': '01',
        'January': '01',
        'Fevereiro': '02',
        'February': '02',
        'Março': '03',
        'Marco': '03',
        'March': '03',
        'Abril': '04',
        'April': '04',
        'Maio': '05',
        'May': '05',
        'Junho': '06',
        'June': '06',
        'Julho': '07',
        'July': '07',
        'Agosto': '08',
        'August': '08',
        'Setembro': '09',
        'September': '09',
        'Outubro': '10',
        'October': '10',
        'Novembro': '11',
        'November': '11',
        'Dezembro': '12',
        'December': '12'
    }

    dt = x.split()
    day = dt[0]
    month = date_map[dt[1]]
    year = dt[2]
    date = '-'.join([year, month, day])

    return date


def translate_city(x):
    city_map = {
        'Lisbon': 'Lisboa',
        'Oporto': 'Porto'
    }

    city = x

    if x in city_map.keys():
        city = city_map[x]

    return city


def translate_contract(x):
    contract_map = {
        'Other': 'Outro',
        'Others': 'Outro',
        'Temporary': 'Temporário',
        'Permanent': 'Permanente',
        'Permenent': 'Permanente',
        'Information not available': 'Informação não disponível',
        'To be defined': 'A definir'
    }

    contract = x

    if x in contract_map.keys():
        contract = contract_map[x]

    return contract


class EraItem(scrapy.Item):
    id = scrapy.Field()
    ref = scrapy.Field()
    job = scrapy.Field()
    main_field = scrapy.Field()
    sub_field = scrapy.Field()
    summary = scrapy.Field()
    vacancies = scrapy.Field()
    contract = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    institute = scrapy.Field()
    deadline = scrapy.Field()
    url = scrapy.Field()
    org_name = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()


class EraLoader(ItemLoader):
    default_output_processor = TakeFirst()

    contract_in = MapCompose(translate_contract)
    contract_out = Join()

    city_in = MapCompose(translate_city)
    city_out = Join()

    summary_in = MapCompose(remove_comments)
    summary_out = Join()

    deadline_in = MapCompose(translate_date)
    deadline_out = Join()
