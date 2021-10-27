from django.db import transaction
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from web.models import Game, Player


class GameSerializer(ModelSerializer):
    player1 = CharField(max_length=256)  # todo: specify address field
    secure_identity = CharField(required=False, read_only=True)

    class Meta:
        model = Game
        fields = ['player1', 'secure_identity']

    def create(self, validated_data):
        with transaction.atomic():
            player1, _ = Player.objects.get_or_create(address=validated_data['player1'])
            validated_data['player1'] = player1
            # validated_data['agent'] = self.context['request'].user
            return super().create(validated_data)
