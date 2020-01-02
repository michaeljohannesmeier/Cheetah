# imports
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from cheetah.spiders import spider4

# start crawler
process = CrawlerProcess(settings=get_project_settings())
#process.crawl(spider1.Spider1)
#process.crawl(spider2.Spider2)
#process.crawl(spider3.Spider3)
#process.crawl(Manga.Manga)
process.crawl(spider4.Runnersworld)
process.start()


#scrapy crawl lauftreff -o lauftreff.csv
