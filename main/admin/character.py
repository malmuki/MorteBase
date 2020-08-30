from django.contrib import admin

from main.models.character import Character, CharacterSkillTree

class CharacterSkillTreeInline(admin.TabularInline):
  model = CharacterSkillTree
  extra = 0

class CharacterAdmin(admin.ModelAdmin):
  list_display = ('name', 'col_skill_trees')
  prepopulated_fields = {'slug': ['name']}
  inlines = [CharacterSkillTreeInline]

  # Custom columns
  def col_skill_trees(self, obj):
    skill_tree_list = []
    for skill_tree in obj.skill_trees.all():
      skill_tree_list.append(str(skill_tree))
    return ', '.join(skill_tree_list)
  col_skill_trees.short_description = 'Skill trees'

admin.site.register(Character, CharacterAdmin)
