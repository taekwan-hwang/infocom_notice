from django.test import TestCase

# Create your tests here.

class SenderTest(TestCase):
	def test_kakao_sender(request):
		from main.sender.sender import KakaoSender
		sender=KakaoSender()
		sender.send_msg("python에서 보낸 메시지입니다")
	
class CrawlerTest(TestCase):
	def test_crawler(request):
		from main.crawler.crawler import Crawler
		crawler=Crawler("http://infocom.ssu.ac.kr/rb/?c=2/38")
		crawler.openurl()
		print(crawler.toBS())
	def test_infocom_crawler(request):
		from main.crawler.infocom_crawler import InfocomCrawler
		crawler=InfocomCrawler()
		new_notices=crawler.get_notices(15)
		for notice in new_notices:
			notice.isSent=True
			notice.save()
		print(crawler.get_new_notices())
