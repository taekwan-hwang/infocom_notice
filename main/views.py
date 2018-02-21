'''Write view here'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.crawler.infocom_crawler import InfocomCrawler
from main.util.regex import find_number_in_string
from main.models import Notice


class Keyboard(APIView):
    '''
    채팅방에 입장했을 때 보여줄 키보드
    '''
    def get(self, request):
        '''
        get 으로 요청
        '''
        return Response({"type":"text"})

class Message(APIView):
    '''
    사용자가 보낸 메시지 처리
    '''
    def post(self, request):
        '''
        post로 요청
        '''
        if request.data['type'] == 'text':
            content = request.data['content']
            try:
                notice_count = find_number_in_string(content)
                crawler = InfocomCrawler()
                notices = crawler.get_notices(notice_count)
                content = Notice.to_msg(notices)
            except IndexError:
                content = "보고싶은 공지사항의 개수를 적어주세요."
            return Response({'message':{'text':content}})
        return Response({'message':{'text':'fail'}})

@api_view(['POST', 'DELETE'])
def pass_request(request, user=''):
    '''
    status code만 정상 응답으로 응답
    http body is empty
    '''
    return Response(status=200)
