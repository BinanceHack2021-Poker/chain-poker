# hardcode for 2 players only: todo
from django.db import models
from django.utils import timezone
import uuid


class Player(models.Model):
    address = models.CharField(unique=True, max_length=256)


class Game(models.Model):
    identifier = models.CharField(max_length=256, unique=True)  # todo: specify exact behaviour
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='created_games')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='joined_games', null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    winner = models.EmailField(null=True, blank=True)  # aka liderboards statistics, etc, etc todo

    # tmp hardcoded rows
    player2_joined = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.identifier = uuid.uuid4().hex
        return super().save(*args, **kwargs)


