from django.contrib.auth.models import User
from django.db import models

from .skill_tree import SkillTree, SkillTreeSkill

CHARACTER_SKILL_TREE_COUNT = 3

class Character(models.Model):
  name = models.CharField(max_length=128)
  slug = models.CharField(max_length=128)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  creation_date = models.DateTimeField(auto_now_add=True)
  skill_trees = models.ManyToManyField(SkillTree, through='CharacterSkillTree')
  currentXP = models.IntegerField(default=5)
  isDead = models.BooleanField(default=False)
  armureMax = models.IntegerField(default=0)

  def save(self, *args, **kwargs):
    saved_already = False

    # Save before checking skill trees if creating model
    if self.id is None:
      super().save(*args, **kwargs)
      saved_already = True

    # Ensure there are 3 skill trees at all time,
    # otherwise reinitialize it
    skill_tree_count = CharacterSkillTree.objects.filter(character=self).count()
    if skill_tree_count < CHARACTER_SKILL_TREE_COUNT:
      for i in range(CHARACTER_SKILL_TREE_COUNT):
        character_skill_tree = CharacterSkillTree(character=self, skillTree=None)
        character_skill_tree.save()
      super().save(*args, **kwargs) # Resave
      saved_already = True

    # Ensure we always save at least once
    if not saved_already:
      super().save(*args, **kwargs)

  def __str__(self):
    return self.name

  def GetMaxHp(self):
    total = 5
    treeSet = CharacterSkillTree.objects.filter(character=self, countForHP=True)
    for tree in treeSet:
      total += tree.GetHpForTree()
    return total

  def GetMaxStamina(self):
    return 5

class CharacterSkillTree(models.Model):
  character = models.ForeignKey(Character, on_delete=models.CASCADE)
  skillTree = models.ForeignKey(SkillTree, blank=True, null=True, on_delete=models.SET_NULL)
  countForHP = models.BooleanField(default=True)

  def __str__(self):
    return str(self.skillTree)

  def GetHpForTree(self):
    hpGrid = SkillTree.objects.get(self.skillTree).GetHPGridPerAttribute()
    return hpGrid[self.GetTierForTree()]

  def GetTierForTree(self):
    return 1

class CharacterSkillTreeSkill(models.Model):
  CharacterSkillTree = models.ForeignKey(CharacterSkillTree, on_delete=models.CASCADE)
  skill = models.ForeignKey(SkillTreeSkill, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return str(self.skill)