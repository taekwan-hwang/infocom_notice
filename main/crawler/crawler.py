from bs4 import BeautifulSoup
from urllib import request, parse

class Crawler():
    def openurl(self, url=None):
        if url==None:
            url=self.url
        
        opener=request.build_opener()
        req=request.Request(url)
        self.opened_url=opener.open(req)
        return self.opened_url
	
    def __init__(self, url=None):
        self.url=url
	
    def to_soup(self, f=None):
        if f==None:
            return BeautifulSoup(self.opened_url, 'html.parser')
        return BeautifulSoup(f, 'html.parser')

    def toHTML(self, f=None):
        if f==None:
            return self.opened_url.read()
        return f.read()