# hardcode for 2 players only: todo
from django.db import models
from django.utils import timezone


class Game(models.Model):
    player1 = models.EmailField()  # aka game creator todo
    player2 = models.EmailField(null=True, blank=True)  # aka joined players todo
    created = models.DateTimeField(default=timezone.now)
    winner = models.EmailField(null=True, blank=True)  # aka liderboards statistics, etc, etc todo
