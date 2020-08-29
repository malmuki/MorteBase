from django.db import models

from .skill import Skill

class Equipement(models.Model):
  SIMPLEWEAPON = "ARS"
  COMBATWEAPON = "ARC"
  WARWEAPON = "ARG"
  THROWNWEAPON = "ARS"
  RANGEWEAPON = "ARD"
  LIGHTARMOR = "ALE"
  HEAVYARMOR = "ALO"
  LIGHTSHIELD = "PBO"
  GREATSHIELD = "GBO"
  EQUIPEMENT = [
    (SIMPLEWEAPON, "Maniement des armes simples"),
    (COMBATWEAPON, "Maniement des armes de combat"),
    (WARWEAPON, "Maniement des armes de guerre"),
    (THROWNWEAPON, "Maniement des armes de jet"),
    (RANGEWEAPON, "Maniement des armes à distance"),
    (LIGHTARMOR, "Port d'armure légère"),
    (HEAVYARMOR, "Port d'armure lourde"),
    (LIGHTSHIELD, "Port des petits boucliers"),
    (GREATSHIELD, "Port des grands boucliers"),
  ]
  equipement = models.CharField(max_length=3, choices=EQUIPEMENT, blank=True, default=SIMPLEWEAPON)

  def __str__(self):
    return str(self.equipement)

  def GetFullName(self):
    di = dict(self.EQUIPEMENT)
    return di[self.equipement]

class SkillTreeSkill(models.Model):
  skillTree = models.ForeignKey("SkillTree", null=True, on_delete=models.CASCADE)
  skill = models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
  requirements = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
  tier = models.PositiveSmallIntegerField(default=0)

  def __str__(self):
    return str(self.skillTree)  + "/" + str(self.skill)

class SkillTree(models.Model):
  name = models.CharField(max_length=128, default='')
  slug = models.CharField(max_length=128, default='')
  description = models.TextField(default='', blank=True)
  restriction = models.ManyToManyField("self", blank=True)
  skill = models.ForeignKey(SkillTreeSkill, blank=True, null=True, on_delete=models.SET_NULL)

  PHYSIQUE = "PHY"
  ESPRIT = "ESP"
  INFLUENCE = "INF"
  ATTRIBUT = [
    (PHYSIQUE, "Physique"),
    (ESPRIT, "Esprit"),
    (INFLUENCE, "Influence"),
  ]
  attribut = models.CharField(max_length=3, choices=ATTRIBUT, blank=True, default=PHYSIQUE)
  equipement = models.ManyToManyField(Equipement)

  def __str__(self):
    return self.name

  def GetHPGridPerAttribute(self):
    if self.attribut == self.PHYSIQUE:
      return (2,4,5)
    elif self.attribut == self.ESPRIT:
      return (2,3,4)
    else:
      return (1,2,3)

  def GetAttibutFullName(self):
    di = dict(self.ATTRIBUT)
    return di[self.attribut]
