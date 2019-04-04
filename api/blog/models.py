from django.db import models

# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Character(models.Model):
    nickname = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    level = models.IntegerField()
    character_class = models.CharField(max_length=50)
    nation = models.CharField(max_length=10)