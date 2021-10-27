from django.urls import path

from web.views import GameView, JoinOrCreateView


app_name = 'web'

urlpatterns = [
    path('', JoinOrCreateView.as_view(), name='join_or_create'),
    path('game/<slug:slug>', GameView.as_view(), name='index'),
]
