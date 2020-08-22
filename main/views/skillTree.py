from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from main.models.skill import Skill
from main.models.skill_tree import SkillTree

class SkillTreeListView(ListView):
  model = SkillTree
  template_name = 'skilltree_list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['nav_skills'] = Skill.objects.all()
    context['nav_skill_trees'] = SkillTree.objects.all()
    return context

class SkillTreeView(DetailView):
  model = SkillTree
  template_name = 'main/skilltree_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['nav_skills'] = Skill.objects.all()
    context['nav_skill_trees'] = SkillTree.objects.all()
    return context