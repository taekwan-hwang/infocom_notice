from. import datafield

class Sender:
	def __init__(self, driver='phantomjs', driverPath='phantomjs'):
		from selenium import webdriver
		if driver == 'phantomjs':
			capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
			capabilities['phantomjs.page.settings.userAgent'] =('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
			self.driver = webdriver.PhantomJS(executable_path=driverPath,desired_capabilities=capabilities, service_args=['--ssl-protocol=any', '--web-security=false'])
		elif driver == 'chrome':
			self.driver=wd.Chrome(executable_path=driverPath)
		self.driver.implicitly_wait(3)
		self._loginkakao()
			
	def _loginkakao(self):
		self.driver.get("https://accounts.kakao.com/login?continue=https://center-pf.kakao.com/signup")
		self.driver.find_element_by_id('email').send_keys(datafield.EMAIL)
		self.driver.find_element_by_id('password').send_keys(datafield.PASSWORD)
		self.driver.find_element_by_id('btn_login').click()
		self.driver.implicitly_wait(3)
		
	def send_msg(self, msg):
		self.driver.get("https://center-pf.kakao.com/_hfvhC/messages/new/feed")
		self.driver.find_element_by_id('messageWrite').send_keys(msg)
		self.driver.find_element_by_css_selector('#mArticle > div > form > div.message_write.message_new > div.info_message > div:nth-child(4) > div > div:nth-child(4) > label > span').click()
		self.driver.implicitly_wait(1)
		self.driver.find_element_by_id('btnName').send_keys('인포컴 바로가기')
		self.driver.find_element_by_id('linkUpload').send_keys('http://infocom.ssu.ac.kr/rb/?c=2/38')
		self.driver.find_element_by_css_selector('#mArticle > div > form > div.wrap_btn > span > button.btn_g.btn_g2').click()
		self.driver.find_element_by_css_selector('#mArticle > div > form > div.wrap_btn > button.btn_g.btn_g2').click()
		self.driver.find_element_by_css_selector('body > div:nth-child(8) > div > div:nth-child(2) > div > div > div.wrap_btn > button.btn_g.btn_g2').click()