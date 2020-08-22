from django.contrib.auth.views import LoginView

from main.models.skill import Skill
from main.models.skill_tree import SkillTree

class LoginView(LoginView):
  template_name = 'main/login.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['nav_skills'] = Skill.objects.all()
    context['nav_skill_trees'] = SkillTree.objects.all()
    return context
