from django.test.runner import DiscoverRunner

class NoDBCreationTestRunner(DiscoverRunner):
	def setup_databases(self, **kwargs):
		pass
	def teardown_databases(self, *args, **kwargs):
		pass