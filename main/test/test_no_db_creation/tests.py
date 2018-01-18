
from django.test import TestCase

class Test(TestCase):
	def test(request):
		"""
		Write your test code here, or create new class, method
		Warning:This test uses exist db, take care of using insert, delete, update new query
		
		when you tests your code, command in terminal : 
		python3 manage.py test main.test.test_no_db_creation.tests.Test.test --settings='main.test..test_no_db_creation.settings'
		
		if you write new class or method, pay attention to the path
		"""