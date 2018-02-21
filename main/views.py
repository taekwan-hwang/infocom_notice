from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.crawler.infocom_crawler import InfocomCrawler
from main.util.regex import find_number_in_string
from main.models import Notice
import re

class Keyboard(APIView):
	def get(self, request):
		return Response({
			"type" : "text",
		})
	
class Message(APIView):
	def post(self, request):
		if request.data['type']=='text':
			content=request.data['content']
			try:
				n=find_number_in_string(content)
				crawler=InfocomCrawler()
				notices=crawler.get_notices(n)
				content=Notice.to_msg(notices)
			except IndexError:
				content="보고싶은 공지사항의 개수를 적어주세요."
			return Response({'message':{'text':content}})
		return Response({'message':{'text':'fail'}})

@api_view(['POST', 'DELETE'])
def passRequest(request, user=''):
	return Response()
