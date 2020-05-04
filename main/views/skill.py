from django.views.generic.list import ListView

from main.models.skill import Skill

class SkillListView(ListView):

  model = Skill

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context