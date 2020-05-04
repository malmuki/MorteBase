from django.urls import path
from django.contrib.auth import views as auth_views

from .views.index import IndexView
from .views.login import LoginView
from .views.signup import SignupView
from .views.SkillTree import SkillTreeListView

app_name = 'main'
urlpatterns = [
    path('connexion/', LoginView.as_view(), name='login'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='logout'),
    path('inscription/', SignupView.as_view(), name='signup'),
    path('mdp_oubli/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('branches/', SkillTreeListView.as_view(), name='branches'),
    path('', IndexView.as_view(), name='index')
]
