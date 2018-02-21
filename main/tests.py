'''
Write test code here
Command : python manage.py test
'''
from django.test import TestCase, Client
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
# Create your tests here.

class SenderTest(TestCase):
    '''
    msg sender test
    '''
    def test_kakao_sender(self):
        '''
        kakao msg sender test
        '''
        from main.sender.sender import KakaoSender
        sender = KakaoSender()
        sender.send_msg("python에서 보낸 메시지입니다")


class CrawlerTest(TestCase):
    '''
    crawler test
    '''
    def test_crawler(self):
        '''
        default crawler test
        '''
        from main.crawler.crawler import Crawler
        crawler = Crawler("http://infocom.ssu.ac.kr/rb/?c=2/38")
        crawler.openurl()
        crawler.to_soup()
        crawler.to_parsed_html()

    def test_infocom_crawler(self):
        '''
        infocom crawler test
        '''
        from main.crawler.infocom_crawler import InfocomCrawler
        crawler = InfocomCrawler()
        new_notices = crawler.get_notices(15)
        for notice in new_notices:
            notice.isSent = True
            notice.save()
        print(crawler.get_new_notices())


class KakaoAdjustTest(TestCase):
    '''
    카카오 플러스친구 api에 적용하는 테스트
    '''
    def _check_status_code(self, response, code=200):
        '''
        예상한 http response status code 가 맞는지 확인
        '''
        if response.status_code != code:
            raise ValueError('unexpected status code')

    def test_keyboard(self):
        '''
        /keyboard 호출 테스트
        '''
        client = Client()
        response = client.get('/main/keyboard')
        self._check_status_code(response)
        json = BytesIO(response.content)
        content = JSONParser().parse(json)
        if content['type'] != 'text':
            raise ValueError('unexpected text')

    def test_message(self):
        '''
        /message 호출 테스트
        '''
        client = Client()
        response = client.post('/main/message',
                               {'user_key': 'test_key', 'type': 'text', 'content': '2개'})
        self._check_status_code(response)
        json = BytesIO(response.content)
        content = JSONParser().parse(json)

        from main.crawler.infocom_crawler import InfocomCrawler

        expected_str = ''
        for notice in InfocomCrawler().get_notices(2):
            expected_str += notice.title+'/'
        expected_str = expected_str[:-1]
        if content['message']['text'] != expected_str:
            raise ValueError('unexpected text')

    def test_pass_request(self):
        '''
        status code 200만 확인하면 되는 테스트들
        '''
        client = Client()
        response = client.post('/main/friend', {'user_key': 'test_key'})
        self._check_status_code(response)
        response = client.delete('/main/friend/user_key')
        self._check_status_code(response)
        response = client.delete('/main/chat_room', {'user_key': 'test_key'})
        self._check_status_code(response)
