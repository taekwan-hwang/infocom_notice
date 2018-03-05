"""
주기적으로 실행해야 할 함수들
"""
import logging
from main.crawler.infocom_crawler import InfocomCrawler
from main.sender.sender import KakaoSender
from main.util.msg_handler import to_msg, set_sent_status
from apscheduler.schedulers.background import BackgroundScheduler


def send_new_msg_to_kakao():
    '''
    카카오톡 플러스친구에 추가된 사람들에게 메세지를 보낸다
    '''
    crawler = InfocomCrawler()
    notices = crawler.get_new_notices()
    if len(notices) == 0:
        return
    msg = '새 공지사항이 등록되었습니다.\r\n\r\n' + to_msg(notices)
    sender = KakaoSender()
    sender.send_msg(msg)
    set_sent_status(notices)


logging.basicConfig(filename='./test.log', level=logging.INFO)
# apscheduler에서 일어나는 모든 정보는 warning이 아니면 무시
logging.getLogger("apscheduler").setLevel(logging.WARNING)
scheduler = BackgroundScheduler()
# interval 형식으로 작동하며, 1시간마다 send_new_msg_to_kakao 실행
scheduler.add_job(send_new_msg_to_kakao, 'interval', seconds=10, max_instances=1)
scheduler.start()
