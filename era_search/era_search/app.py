#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

era_search = Flask(__name__)

# TODO: Configuration
host = "http://localhost:9200"
index_name = "eracareers"
aggregation_fields = ["city", "vacancies", "contract", "main_field", "sub_field"]

es = Elasticsearch(host)


@era_search.route('/')
def index():
    term = "*"

    results = perform_query(term, "", 0)

    return render_template('index.html', results=results, term=term, page=1)


@era_search.route('/search')
def search():
    term = request.args.get('term', '')
    filters = request.args.get('filter', '')
    page = request.args.get('page', '')

    if not term or term == "null":
        term = "*"

    results = perform_query(term, filters, page)

    return render_template('index.html', results=results, filters=filters, term=term, page=page)


def perform_query(term, filter_string, page):
    filters = parse_filters(filter_string)

    term = term.encode('utf-8')
    query = get_basic_query(filters, term, page)

    result = es.search(index=index_name, body=query)

    return result


def parse_filters(filters):
    filter_dict = {}
    for f in filters.split(','):
        if f and len(f.split('-')) == 2:
            typ = f.split('-')[0].encode('utf-8')
            val = f.split('-')[1].encode('utf-8')
            filter_dict[typ] = val

    return filter_dict


# Those queries implement the filters as AND filter and the query as query_string_query
def get_basic_query(filters, term, page):
    query = None

    if not page:
        page = 0

    start = int(page) * 12  # Number of results per page

    must_clauses = []

    for k, v in filters.iteritems():
        clause = {
            "term": {k: v}
        }

        must_clauses.append(clause)

        filter_clauses = {"and": must_clauses}

    aggregations = {}

    for el in aggregation_fields:
        aggregations[el] = {"terms": {"field": el}}

    if term and filters:
        query = {
            "query": {
                "filtered": {
                    "filter": filter_clauses,
                    "query": {
                        "query_string": {
                            "query": term
                        }
                    }
                }
            },
            "size": 12,
            "from": start,
            "aggs": aggregations
        }

    elif term:
        query = {
            "query": {
                "query_string": {
                    "query": term
                }
            },
            "size": 12,
            "from": start,
            "aggs": aggregations
        }

    return query

