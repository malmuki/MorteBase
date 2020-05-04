from django.views.generic.base import TemplateView

from main.models.skill_tree import SkillTree

class IndexView(TemplateView):
  template_name = 'main/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['nav_skill_trees'] = SkillTree.objects.all()
    return context
