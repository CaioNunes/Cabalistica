from rest_framework import serializers
from blog.models import Player
from blog.models import Character

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'