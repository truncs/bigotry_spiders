from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz.org"
    allowed_domains = ["dmoz.org"]
    start_urls = [
         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        #hxs.select('/html/body/div[@id="cnnContainer"]/div[@id="cnnContentContainer"]/div[@id="cnnSnapShot"]/div[@id="cnnHeaderLeftCol"]/h1/text()').extract()


        
        
