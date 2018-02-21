"""
주기적으로 실행해야 할 함수들
"""
from main.crawler.infocom_crawler import InfocomCrawler
from main.sender.sender import KakaoSender
from main.models import Notice


def send_new_msg_to_kakao():
    '''
    카카오톡 플러스친구에 추가된 사람들에게 메세지를 보낸다
    '''
    crawler = InfocomCrawler()
    notices = crawler.get_new_notices()
    msg = Notice.to_msg(notices)
    sender = KakaoSender()
    sender.send_msg(msg)
