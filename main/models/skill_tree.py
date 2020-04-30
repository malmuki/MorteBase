from django.db import models

from .skill import Skill

class SkillTree(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField(default=' ')
  restriction = models.ManyToManyField("self", blank=True)
  skill = models.ManyToManyField(Skill, blank=True, through='SkillTreeSkill')
  
  def __str__(self):
    return self.name

class SkillTreeSkill(models.Model):
  SkillTree = models.ForeignKey(SkillTree, null=True, on_delete=models.CASCADE)
  skill = models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
  requirements = models.ManyToManyField("self")
  
  def __str__(self):
    return str(self.skill_tree)