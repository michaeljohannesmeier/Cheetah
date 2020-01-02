import string
import scrapy
#from scrapy import Request
from ..env import environ

class Spider4(scrapy.Spider):

    name = environ['spider4']['name']
    allowed_domains = environ['spider4']['allowed_domains']
    start_urls = environ['spider4']['start_url']

    def parse(self, response):
        counter = 0
        yield scrapy.Request(f'{environ["spider4"]["start_url"]}/?p={counter}', callback=self.parse_runs, meta={'counter': counter})

    def parse_runs(self, response):
        counter = response.request.meta['counter']
        if len(response.xpath('//div[@class="v-A_-appointment__entry__inner"]')) > 0:
            for run_info in response.xpath('//div[@class="v-A_-appointment__entry__inner"]'):
                yield {
                    "Name": run_info.xpath(
                        './/span[@class="v-A_-headline v-A_-headline--gamma"]/text()').extract_first().strip(),
                    "Distance": run_info.xpath('.//div[@class="v-A_-distance"]/span/text()').extract(),
                    "Date": run_info.xpath('./div[@class="v-A_-appointment__entry__date"]/span/text()').extract(),
                    "Location": run_info.xpath('.//span[@class="v-A_-location"]/text()').extract_first().strip(),

                }
            counter += 1
            yield scrapy.Request(f'{environ["spider4"]["start_url"]}/?p={counter}', callback=self.parse_runs, meta={'counter': counter})

