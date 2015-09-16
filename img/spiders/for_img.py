import scrapy
import urllib
import re

class ImgSpider(scrapy.Spider):
    name = "forimg"
    allowed_domains = ["tp123456.com"]
    start_urls = ["http://img.tp123456.com/Html/54018.html",]

    def parse(self,response):
        url = response.xpath('//img/@src').extract()
        x = 0
        for imgurl in url:
            imgurl = 'http://img.tp123456.com'+imgurl
            urllib.urlretrieve(imgurl,'%s.jpg' %x )
            x+=1
