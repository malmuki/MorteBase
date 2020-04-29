# Models with additional config
from .character import CharacterAdmin

# Other models
from django.contrib import admin

from main.models.skill import Skill
admin.site.register(Skill)

from main.models.skill_tree import SkillTree
admin.site.register(SkillTree)
