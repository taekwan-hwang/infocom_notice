from django.db import models

# Create your models here.
class Notice(models.Model):
	url=models.CharField(max_length=100, null=False)
	title=models.CharField(max_length=100, null=False)
	date=models.DateField()
	added_date=models.DateField(auto_now_add=True)
	views=models.IntegerField()