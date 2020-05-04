from django.db import models

from .skill import Skill

class SkillTree(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField(default=' ')
  restriction = models.ManyToManyField("self", blank=True)
  skill = models.ManyToManyField(Skill, blank=True, through='SkillTreeSkill')
  
  PHYSIQUE = "PHY"
  ESPRIT = "ESP"
  INFLUENCE = "INF"
  ATTRIBUT = [
    (PHYSIQUE, "Physique"),
    (ESPRIT, "Esprit"),
    (INFLUENCE, "Influence"),
  ]
  attribut = models.CharField(max_length=3, choices=ATTRIBUT, blank=True, default=PHYSIQUE)

  #SIMPLEWEAPON
  #equipement = 

  def __str__(self):
    return self.name

  def GetHPGridPerAttribute(self):
    if self.attribut == self.PHYSIQUE:
      return (2,4,5)
    elif self.attribut == self.ESPRIT:
      return (2,3,4)
    else:
      return (1,2,3)


class SkillTreeSkill(models.Model):
  skillTree = models.ForeignKey(SkillTree, null=True, on_delete=models.CASCADE)
  skill = models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
  requirements = models.ManyToManyField("self")
  tier = models.PositiveSmallIntegerField(default=0)
  
  def __str__(self):
    return str(self.skillTree)