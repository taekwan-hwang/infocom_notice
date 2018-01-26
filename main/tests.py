from django.test import TestCase

# Create your tests here.

class SenderTest(TestCase):
	from main.sender.sender import Sender
	sender=Sender()
	sender.loginkakao()
	sender.send_msg("python에서 보낸 메시지입니다")