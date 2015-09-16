 
import urllib
import urllib2
import re

class Spider:
 
    def __init__(self):
        self.siteURL = 'http://img.tp123456.com'
 
    def getPage(self,pageIndex):
        url = self.siteURL + "/Html/Html18-" + str(pageIndex) + ".html"
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
 
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<li>.*?<h2><a href="(.*?)".*?blank">(.*?)</a>.*?other">(.*?)</span>.*?</li>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item[0],item[1]

spider = Spider()
spider.getContents(3)
