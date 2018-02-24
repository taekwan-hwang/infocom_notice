'''
Notice 의 쿼리셋들을 다루는 모듈
'''

def to_msg(notices):
    '''
    쿼리셋을 전송할 메시지로 변경하는 메소드
    '''
    msg = ''
    for notice in notices:
        msg += notice.title + '/'
    return msg[:-1]

def set_sent_status(notices):
    '''
    보낸 상태로 만드는 메소드
    '''
    for notice in notices:
        notice.isSent = True
        notice.save()
