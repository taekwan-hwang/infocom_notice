from django.test import TestCase
from django.test import Client
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
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

class KakaoAdjustTest(TestCase):
	def _check_status_code(self, response, code=200):
		if response.status_code != code:
			raise ValueError('unexpected status code')
			
	def testKbd(self):
		client=Client()
		response=client.get('/main/keyboard')
		self._check_status_code(response)
		json=BytesIO(response.content)
		content=JSONParser().parse(json)
		if content['type'] != 'text':
			raise ValueError('unexpected text')
		
	def testMsg(self):
		client=Client()
		response = client.post('/main/message', {'user_key':'test_key', 'type':'text', 'content':'hi'})
		self._check_status_code(response)
		json=BytesIO(response.content)
		content=JSONParser().parse(json)
		if content['message']['text'] != 'hi':
			raise ValueError('unexpected text')
			
	def testPassRequest(self):
		client=Client()
		response=client.post('/main/friend', {'user_key':'test_key'})
		self._check_status_code(response)
		response=client.delete('/main/friend/user_key')
		self._check_status_code(response)
		response=client.delete('/main/chat_room', {'user_key':'test_key'})
		self._check_status_code(response)
