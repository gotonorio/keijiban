from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from register.forms import LoginForm
# from django.contrib.auth.models import Permission


User = get_user_model()


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'register/logout.html'
