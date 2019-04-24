from django.db import models
from django.utils import timezone

class User(models.Model):
  user_name = models.CharField(max_length=255)
  email = models.EmailField()
  total_games = models.PositiveSmallIntegerField(default=0)
  won_games = models.PositiveSmallIntegerField(default=0)

  def __str__(self):
    return self.user_name 

class Image(models.Model):
  user_id = models.PositiveSmallIntegerField(default=1)
  image_name = models.CharField(max_length=255, unique=True)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'User ID: {self.userID} - Image Name: {self.image_name}'

class Clue(models.Model):
  attribute = models.CharField(max_length=255)
  clue_text = models.TextField()

  def __str__(self):
    return f'{self.attribute} - Clue: {self.clue_text}'
