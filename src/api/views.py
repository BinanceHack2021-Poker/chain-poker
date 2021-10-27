from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from api.serializers import GameSerializer


class CreateGameApiView(CreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [AllowAny]  # todo
