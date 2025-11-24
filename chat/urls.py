from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('ask/', views.ask_question, name='ask_question'),
    path('clear/', views.clear_chat, name='clear_chat'),
]
