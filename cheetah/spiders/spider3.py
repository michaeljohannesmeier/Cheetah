# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..env import environ


class Spider3(scrapy.Spider):
    name = environ['spider3']['name']
    allowed_domains = environ['spider3']['allowed_domains']
    start_urls = environ['spider3']['start_url']

    def parse(self, response):
        rows = response.xpath('//table[@class="w100pr liste"]//tr')
        for row in rows:
            date = row.xpath('normalize-space(.//td[3]/a/text())').get()
            name = row.xpath('normalize-space(.//td[5]/a/text())').get()
            location = row.xpath('normalize-space(.//td[6]/a/text())').get()
            distances = row.xpath('normalize-space(.//td[7]/a/text())').get()
            url = row.xpath('.//td[7]/a/@href').get()
            absolute_url = response.urljoin(url)

            yield {
                'Date': date,
                'Name': name,
                'Distance': distances,
                'Location': location,
                'Url': absolute_url
                 }

        next_urls = response.xpath("//div[@id='listenavi']//a/@href").extract()
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse)

            #if date and name and distances:
            #    absolute_url = response.urljoin(url)
                #yield scrapy.Request(absolute_url, self.get_sub_url, meta={'name': name, 'sub_url': url, 'distance': distances})
             #   yield scrapy.Request(absolute_url)

    # def get_sub_url(self, response):
    #     #address = response.xpath('//div[@class="lk-adr"][position() > 1]/text()').getall()
    #     # distances = response.xpath('//div[@class="lk-renn"][position() > 1]/text()').getall()
    #     # result_list = response.xpath('//div[@class="lk-ergb"][position() > 1]/text()').getall()
    #     # date = response.xpath('//div[@class="lk-dat"]/text()').get()
    #     yield {
    #         #'address': address,
    #         'name': response.request.meta['name'],
    #         'distance': response.request.meta['distances'],
    #         # 'result_list': result_list,
    #         'date': response.request.meta['date']
    #     }

