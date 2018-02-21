'''
django models
'''
from django.db import models

# Create your models here.
class Notice(models.Model):
    '''
    공지사항 정보
    '''
    uid = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=100, null=False)#path
    title = models.CharField(max_length=100, null=False)#name
    posted_date = models.DateField()
    added_in_db_date = models.DateField(auto_now_add=True)
    views = models.IntegerField()#조회수
    isSent = models.BooleanField(default=False)

    @staticmethod
    def to_msg(notices):
        '''
        쿼리셋을 전송할 메시지로 변경하는 메소드
        '''
        msg = ''
        for notice in notices:
            msg += notice.title+'/'
        return msg[:-1]
