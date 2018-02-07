from django.db import models

# Create your models here.
class Notice(models.Model):
	uid=models.IntegerField(primary_key=True)
	url=models.CharField(max_length=100, null=False)#path
	title=models.CharField(max_length=100, null=False)#name
	posted_date=models.DateField()
	added_in_db_date=models.DateField(auto_now_add=True)
	views=models.IntegerField()#조회수
	isSent=models.BooleanField(default=False)