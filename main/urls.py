from django.urls import path
from main import views

urlpatterns = [
	path('keyboard', views.Keyboard.as_view()),
	path('message', views.Message.as_view()),
	path('friend', views.passRequest),
	path(r'friend/<str:user>', views.passRequest),
	path('chat_room', views.passRequest),
]