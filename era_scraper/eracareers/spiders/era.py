# -*- coding: utf-8 -*-

import scrapy
from eracareers.items import EraItem, EraLoader


class EraSpider(scrapy.Spider):
    name = "era"
    allowed_domains = ["eracareers.pt"]
    start_urls = (
        'http://www.eracareers.pt/search/index.aspx?task=search&idc=1',
    )

    def parse(self, response):
        # Start with a search with no terms to get all results
        req = scrapy.FormRequest.from_response(
            response,
            dont_filter=True,
            dont_click=True,
            formdata={
                '__VIEWSTATE': '/wEPDwUKMTc0MDUzNzk4MQ9kFgJmD2QWAgIBD2QWAgIED2QWAmYPZBYKZg8PFgIeBFRleHQFATFkZAIBDw8WAh8ABQZzZWFyY2hkZAIIDxAPFgIeC18hRGF0YUJvdW5kZ2QQFSkkRXNjb2xoYSB1bWEgb3DDp8Ojby9DaG9vc2UgYW4gb3B0aW9uFUFncmljdWx0dXJhbCBzY2llbmNlcyhBbmltYWwgU2NpZW5jZSBhbmQgVmV0ZXJpbmFyaWFuIFNjaWVuY2VzDEFudGhyb3BvbG9neQxBcmNoaXRlY3R1cmUEQXJ0cwlBc3Ryb25vbXkTQmlvbG9naWNhbCBzY2llbmNlcwlDaGVtaXN0cnkWQ29tbXVuaWNhdGlvbiBzY2llbmNlcxBDb21wdXRlciBzY2llbmNlC0NyaW1pbm9sb2d5EEN1bHR1cmFsIHN0dWRpZXMKRGVtb2dyYXBoeR1FYXJ0aCBhbmQgQXRtb3NwaGVyZSBTY2llbmNlcwlFY29ub21pY3MURWR1Y2F0aW9uYWwgc2NpZW5jZXMLRW5naW5lZXJpbmcVRW52aXJvbm1lbnRhbCBzY2llbmNlGUV0aGljcyBpbiBoZWFsdGggc2NpZW5jZXMaRXRoaWNzIGluIG5hdHVyYWwgc2NpZW5jZXMbRXRoaWNzIGluIHBoeXNpY2FsIHNjaWVuY2VzGUV0aGljcyBpbiBzb2NpYWwgc2NpZW5jZXMJR2VvZ3JhcGh5B0hpc3RvcnkTSW5mb3JtYXRpb24gc2NpZW5jZRJKdXJpZGljYWwgc2NpZW5jZXMRTGFuZ3VhZ2Ugc2NpZW5jZXMKTGl0ZXJhdHVyZQtNYXRoZW1hdGljcxBNZWRpY2FsIHNjaWVuY2VzDU5ldXJvc2NpZW5jZXMNTm90IGF2YWlsYWJsZRhQaGFybWFjb2xvZ2ljYWwgc2NpZW5jZXMKUGhpbG9zb3BoeQdQaHlzaWNzElBvbGl0aWNhbCBzY2llbmNlcxZQc3ljaG9sb2dpY2FsIHNjaWVuY2VzElJlbGlnaW91cyBTY2llbmNlcwlTb2Npb2xvZ3kKVGVjaG5vbG9neRUpATACOTMDNDA1AzE4NwMzMjcCMTkDMTE4AzEwMwMxMjEDMTk0AzEzOAMyMDYDMjA3AzIyNwM0MDQDMjI4AzI2OAMzMzEDMTExATEDMTE3AzE1MQMyNzMDMjc0AjI2AjUzAzI4MgI1OQI2MwMxNTIBMgE1AzQwMwIxMgI3NAMxNjYDMzA0AzMxMAI4NgMzMTUDMzYxFCsDKWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZGQCDg8PFgIfAAVaRm91bmQgPGI+NTU1PC9iPiByZXN1bHRzIGluIDxiPjU1NTwvYj4gcmVzZWFyY2ggb3Bwb3J0dW5pdGllcy4gUGFnZSA8Yj4xPC9iPiBvZiA8Yj41NjwvYj4uZGQCEQ8PFgIeB0VuYWJsZWRnZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFIFRlbXBsYXRlSW50ZXJuYTE6X2N0bDA6Q2hlY2tCb3gxBSBUZW1wbGF0ZUludGVybmExOl9jdGwwOkNoZWNrQm94MjfLPVgd4t3q4A47FXPeSEOsnEeU',
                '__EVENTVALIDATION': '/wEWBwK59PaeBgKMu4v7BALq8vIdAvTy8h0C6/LyHQL3tejtDwKzyeOyDTrt8KCiHxIB3jFhyNaoseirV3Sp',
                'TemplateInterna1:_ctl0:DropDownList2': '2',
                'TemplateInterna1:_ctl0:Button1': 'OK'
            },
            callback=self.get_results
        )

        return req

    def get_results(self, response):
        base_url = 'http://www.eracareers.pt'
        jobs = []

        for link in response.xpath('.//div[@class="DIVresultadoPesquisa"]/a/@href').extract():
            jobs.append(base_url + link)

        viewstate = response.xpath('.//input[@name="__VIEWSTATE"]/@value').extract()
        eventvalidation = response.xpath('.//input[@name="__EVENTVALIDATION"]/@value').extract()

        if jobs:
            for job in jobs:
                yield scrapy.Request(job, callback=self.get_job)

        if response.xpath('.//a[@id="TemplateInterna1__ctl0_LinkButton2"]').extract():
            req = scrapy.FormRequest.from_response(
                response,
                dont_filter=True,
                dont_click=True,
                formdata={
                    '__EVENTTARGET': 'TemplateInterna1$_ctl0$LinkButton2',
                    '__VIEWSTATE': viewstate,
                    '__EVENTVALIDATION': eventvalidation,
                    'TemplateInterna1:_ctl0:DropDownList2': '2',
                },
                callback=self.get_results
            )

            yield req

    def get_job(self, response):
        l = EraLoader(item=EraItem(), response=response)

        l.add_value('id', response.xpath(u'normalize-space(.//td[contains(text(), "Unique identifier")]/following-sibling::td/text())').extract())
        l.add_value('job', response.xpath(u'normalize-space(.//div[@id="TemplateInterna1__ctl0_Panel1"]/text()[preceding-sibling::br[preceding-sibling::b[contains(text(), "Cargo") or contains(text(), "Job")]] and following-sibling::br])').extract())
        l.add_value('ref', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Referência") or contains(text(), "Job/Fellowship Reference")]])').extract())
        l.add_value('main_field', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Área científica genérica") or contains(text(), "Main research field")]])').extract())
        l.add_value('sub_field', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Área científica específica") or contains(text(), "Sub research field")]])').extract())
        l.add_value('summary', response.xpath(u'normalize-space(string(//*[@id="Table1" and @class="DIVresultadoPesquisaGlobal"]/tr[4]/td))').extract())
        l.add_value('vacancies', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Número de vagas") or contains(text(), "Vacant posts")]])').extract())
        l.add_value('contract', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Tipo de contrato") or contains(text(), "Type of contract")]])').extract())
        l.add_value('country', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "País") or contains(text(), "Job country")]])').extract())
        l.add_value('city', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Localidade") or contains(text(), "Job city")]])').extract())
        l.add_value('institute', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Instituição") or contains(text(), "Job company")]])').extract())
        l.add_value('deadline', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Data limite") or contains(text(), "deadline")]])').extract())
        l.add_value('org_name', response.xpath(u'normalize-space(.//td/text()[preceding-sibling::b[contains(text(), "Instituição de contacto") or contains(text(), "Organization/institute")]])').extract())
        l.add_value('email', response.xpath(u'normalize-space(.//td/a[preceding-sibling::b[contains(text(), "Email")]])').extract())
        l.add_value('website', response.xpath(u'normalize-space(.//td/a[preceding-sibling::b[contains(text(), "Website")]])').extract())
        l.add_value('url', response.url)

        yield l.load_item()
