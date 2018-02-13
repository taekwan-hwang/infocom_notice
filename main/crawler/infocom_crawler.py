from .crawler import Crawler
import requests
from bs4 import BeautifulSoup
from main.models import Notice

class InfocomCrawler(Crawler):
	"""need implementation 2 method"""
	def __init__(self):
		url = 'http://infocom.ssu.ac.kr/rb/?c=2/38'
		Crawler.__init__(self, url)
	def get_notices(self, n):
		notices=[]
		Crawler.openurl(self)
		soup = Crawler.toBS(self)
		noticeSubcon = soup.find("div", {"class": "subcon"})
		noticeList = noticeSubcon.find_all("div", {"class": "list"})
		for item in noticeList:
			href = item.get('onclick')
			ref = href.split('&')[1].split("'")
			noticeUrl = self.url + '&' + ref[0]
			uid = noticeUrl.split('=')[2]
			title = item.find("span", {"class": "subject"}).text
			info = item.find("div", {"class": "info"}).text
			info = info.split()
			posted_date = info[2].replace('.', '-')
			views = info[6]
			notices.append({'uid': uid, 'title': title, 'url': noticeUrl, 'posted_date': posted_date, 'views': views})
		notices = sorted(notices, key = lambda k:k['uid'], reverse=True)
		notice = notices[0:n]
		for item in notice:
			n = Notice()
			n.uid = item['uid']
			n.url = item['url']
			n.title = item['title']
			n.posted_date = item['posted_date']
			n.views = item['views']
			n.save()
		return notice
	def get_new_notices(self):
		pass