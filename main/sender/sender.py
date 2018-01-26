from. import datafield
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
import django
django.setup()

class Sender:
	def __init__(self, driver='phantomjs', driverPath='/workspace/dev/infocom_notice/main/sender/phantomjs'):
		#os.environ['NO_PROXY'] = '127.0.0.1'
		from selenium import webdriver as wd
		if driver == 'phantomjs':
			self.driver=wd.PhantomJS(executable_path=driverPath)
		elif driver == 'chrome':
			self.driver=wd.Chrome(executable_path=driverPath)
			
	def loginkakao(self):
		self.driver.get("https://accounts.kakao.com/login?continue=https://center-pf.kakao.com/signup")
		self.driver.find_element_by_id('email').send_keys(datafield.EMAIL)
		self.driver.find_element_by_id('password').send_keys(datafield.PASSWORD)
		self.driver.find_element_by_id('btn_login').click()
		self.driver.implicitly_wait(3)
		
	def send_msg(self, msg):
		self.driver.get("https://center-pf.kakao.com/_hfvhC/messages/new/feed")
		self.driver.find_element_by_id('messageWrite').send_keys(msg)
		self.driver.find_element_by_id('fieldRadio3Foritems[0].link.type').click()
		self.driver.implicitly_wait(1)
		self.driver.find_element_by_id('btnName').send_keys('인포컴 바로가기')
		self.driver.find_element_by_id('linkUpload').send_keys('http://infocom.ssu.ac.kr/rb/?c=2/38')
		self.driver.find_element_by_css_selector('#mArticle > div > form > div.wrap_btn > span > button.btn_g.btn_g2').click()
		self.driver.find_element_by_css_selector('#mArticle > div > form > div.wrap_btn > button.btn_g.btn_g2').click()