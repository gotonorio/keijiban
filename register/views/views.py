from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic

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


class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "register/mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_id'] = self.request.user.id
        return context


class MasterPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "register/master_data.html"


class OperateDataView(LoginRequiredMixin, generic.TemplateView):
    template_name = "register/operate_data.html"


class OperateRepairDataView(LoginRequiredMixin, generic.TemplateView):
    template_name = "register/operate_repair_data.html"


class MasterDataView(LoginRequiredMixin, generic.TemplateView):
    template_name = "register/master_data.html"