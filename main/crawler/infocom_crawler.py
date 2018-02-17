from .crawler import Crawler
from main.models import Notice

class InfocomCrawler(Crawler):
	def __init__(self):
		url = 'http://infocom.ssu.ac.kr/rb/?c=2/38'
		Crawler.__init__(self, url)

	def get_notices(self, n=None):
		Crawler.openurl(self)
		notice_milestone = Crawler.toBS(self).find("div", {"class": "subcon"})
		notice_list = notice_milestone.find_all("div", {"class": "list"})
		notice_list=sorted(notice_list, key=lambda k:k.get('onclick').split('&')[1].split("'")[0], reverse=True)

		if n is not None:
			notice_list=notice_list[0:n]

		notices = []

		for notice_info in notice_list:
			# parsing uid
			uid=notice_info.get('onclick').split('&')[1].split("'")[0].split('=')[1]

			# save data if not in db
			try:
				notice = Notice.objects.get(uid=uid)
			except Notice.DoesNotExist:
				#parsing data
				url = self.url + '&uid=' + uid
				title = notice_info.find("span", {"class": "subject"}).text
				info = notice_info.find("div", {"class": "info"}).text.split()
				posted_date = info[2].replace('.', '-')
				views = info[6]
				#save data in db
				notice = Notice()
				notice.uid = uid
				notice.url = url
				notice.title = title
				notice.posted_date = posted_date
				notice.views = views
				notice.save()
			finally:
				notices.append(notice)
		return notices

	def get_new_notices(self):
		pass