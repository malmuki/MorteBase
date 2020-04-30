from django.db import models

class Skill(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField(default=' ')

  def __str__(self):
    return self.name
