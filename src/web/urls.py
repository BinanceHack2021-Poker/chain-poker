from django.urls import path

from web.views import IndexView, JoinOrCreateView


app_name = 'web'

urlpatterns = [
    path('', JoinOrCreateView.as_view(), name='join_or_create'),
    path('game/<slug:slug>', IndexView.as_view(), name='index'),
]
