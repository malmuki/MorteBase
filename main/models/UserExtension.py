from django.contrib.auth.models import User
from django.db import models
from .character import Character

class UserExtension(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  activeCharacter = models.ForeignKey(Character, blank=True, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.user
