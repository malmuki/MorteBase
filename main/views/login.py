from django.contrib.auth.views import LoginView

from main.models.skill_tree import SkillTree

class LoginView(LoginView):
  template_name = 'main/login.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['skill_trees'] = SkillTree.objects.all()
    return context
