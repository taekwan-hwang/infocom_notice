from bs4 import BeautifulSoup
from urllib import request, parse

class Crawler():
	def __init__(url=None):
        self.url=url
        if url!=None:
            self.opened_url=openurl(url)
	
	def openurl(self, url=None, handlers=[]):
        if url==None:
            url=self.url
        
        opener=request.build_opener(handlers)
        req=request.Request(url)
        self.opened_url=opener.open(req)
        return self.opened_url
	
	def toBS(f=None):
        if f==None:
            return BeautifulSoup(self.opened_url, 'lxml')
        return BeautifulSoup(f, 'lxml')

    def toHTML(f=None):
        if f==None:
            return self.opened_url.read()
        return f.read()