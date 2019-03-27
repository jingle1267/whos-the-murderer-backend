from django.db import models
from django.utils import timezone

class User(models.Model):
  user_name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__(self):
    return self.user_name 

class Game(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
  is_won = models.BooleanField()
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'Game ID: {self.gameID} belongs to User {self.userID}'

class Image(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
  image_name = models.CharField(max_length=255, unique=True)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'User ID: {self.userID} - Image Name: {self.image_name}'

class Clue(models.Model):
  attribute = models.CharField(max_length=255)
  clue_text = models.TextField()

  def __str__(self):
    return f'{self.attribute} - Clue: {self.clue_text}'
