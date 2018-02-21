'''django url pattern matching'''
from django.urls import path
from main import views


urlpatterns = [
    path('keyboard', views.Keyboard.as_view()),
    path('message', views.Message.as_view()),
    path('friend', views.pass_request),
    path(r'friend/<str:user>', views.pass_request),
    path('chat_room', views.pass_request),
]
