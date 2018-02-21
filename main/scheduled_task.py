from main.crawler.infocom_crawler import InfocomCrawler
from main.sender.sender import KakaoSender

def send_new_msg_to_kakao():
	crawler=InfocomCrawler()
	msg=crawler.get_new_notices()
	sender=KakaoSender()
	sender.send_msg(msg)