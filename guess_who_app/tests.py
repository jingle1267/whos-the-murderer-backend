from django.test import TestCase
from .models import *
import redgreenunittest as unittest

class BackEndTestCase(TestCase):
  def setUp(self):
    self.user = User(user_name="Wynspeare", email="w@w.com")
    # self.user.save()
    self.image = Image(user_id=1, image_name="test_image")
    # self.image.save()
    self.clue  = Clue(attribute="hat", clue_text="The murderer is wearing a hat")
    # self.clue.save()

  # def test_01_users_image(self):
  #   """returns the users image"""
  #   wynspeare = User.objects.get(user_name="Wynspeare")
  #   w_image = Image.objects.get(user_id=1)
  #   self.assertEqual(wynspeare.user_id, user)
