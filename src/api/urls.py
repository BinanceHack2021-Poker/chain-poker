from django.urls import path

from api.views import CreateGameApiView

app_name = 'api'

urlpatterns = [
    path('game', CreateGameApiView.as_view(), name='create_game'),
]
