from django.db import models
from django.contrib.auth.models import User  # Используйте стандартную модель пользователя

class Game(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Используйте стандартную модель пользователя
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    is_alive = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)  # Поле для хранения результата игры: 'Win' или 'Loss'
