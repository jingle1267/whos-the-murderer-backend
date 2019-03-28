from rest_framework import serializers
from .models import User, Image, Clue

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['user_name', 'email', 'total_games', 'won_games', 'id']

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ['id', 'image_name', 'user_id']

class ClueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clue
    fields = ['id', 'attribute', 'clue_text']