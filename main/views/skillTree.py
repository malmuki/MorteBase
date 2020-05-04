from django.views.generic.list import ListView

from main.models.skill_tree import SkillTree

class SkillTreeListView(ListView):

  model = SkillTree

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context
