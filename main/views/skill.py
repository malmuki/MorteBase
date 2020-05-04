from django.views.generic.list import ListView

from main.models.skill import Skill
from main.models.skill_tree import SkillTree

class SkillListView(ListView):
  model = Skill

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['nav_skill_trees'] = SkillTree.objects.all()
    return context
