from django.contrib import admin

from main.models.skill_tree import SkillTree, SkillTreeSkill, Equipement

class SkillTreeSkillInline(admin.TabularInline):
  model = SkillTreeSkill
  fields = ['skill']
  extra = 0

class SkillTreeAdmin(admin.ModelAdmin):
  list_display = ('name', 'col_skill')
  prepopulated_fields = {'slug': ['name']}
  inlines = [SkillTreeSkillInline]

  # Custom columns
  def col_skill(self, obj):
    skill_list = []
    for skills in obj.skill.all():
      skill_list.append(str(skills))
    return ', '.join(skill_list)
  col_skill.short_description = 'Skill'

admin.site.register(SkillTree, SkillTreeAdmin)
admin.site.register(Equipement)
admin.site.register(SkillTreeSkill)