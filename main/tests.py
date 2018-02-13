from django.test import TestCase

# Create your tests here.

class SenderTest(TestCase):
	def test_kakao_sender(request):
		from main.sender.sender import Sender
		sender=Sender()
		sender.loginkakao()
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
		print(crawler.get_notices(3))