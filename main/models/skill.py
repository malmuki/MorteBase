from django.db import models

from .skill_tree import SkillTree

class Skill(models.Model):
  name = models.CharField(max_length=128)
  skill_tree = models.ForeignKey(SkillTree, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.name
