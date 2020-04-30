# Models with additional config
from .character import CharacterAdmin
from .skill_tree import SkillTreeAdmin

# Other models
from django.contrib import admin

from main.models.skill import Skill
admin.site.register(Skill)
