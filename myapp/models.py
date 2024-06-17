from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass  # Исходная модель без поля balance

class Game(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Player(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    is_alive = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)  # Поле для хранения результата игры: 'Win' или 'Loss'
