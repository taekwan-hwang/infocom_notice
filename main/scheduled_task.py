"""
주기적으로 실행해야 할 함수들
"""
from main.crawler.infocom_crawler import InfocomCrawler
from main.sender.sender import KakaoSender
from main.util.msg_handler import to_msg, set_sent_status


def send_new_msg_to_kakao():
    '''
    카카오톡 플러스친구에 추가된 사람들에게 메세지를 보낸다
    '''
    crawler = InfocomCrawler()
    notices = crawler.get_new_notices()
    if len(notices) == 0:
        return
    msg = to_msg(notices)
    sender = KakaoSender()
    sender.send_msg(msg)
    set_sent_status(notices)
