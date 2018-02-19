from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.crawler.infocom_crawler import InfocomCrawler
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
                        n=int(re.findall('\d+', content)[0])
                        crawler=InfocomCrawler()
                        notices=crawler.get_notices(n)
                        res=""
                        for notice in notices:
                            res += notice.title+" "
                        content=res
			return Response({'message':{'text':content}})
		return Response({'message':{'text':'fail'}})

@api_view(['POST', 'DELETE'])
def passRequest(request, user=''):
	return Response()
