from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models.aggregates import Max
from django.shortcuts import render
from django.views import generic

from bbs.forms import SwitchCSSForm
from bbs.models import File


# class KeijibanView(PermissionRequiredMixin, generic.TemplateView):
class KeijibanView(generic.TemplateView):
    """掲示板表示"""

    model = File
    template_name = "bbs/keijiban.html"
    # permission_required = "bbs.add_file"

    def get_template_names(self):
        """templateファイルを切り替える"""
        if self.request.user_agent_flag == "mobile":
            template_name = "bbs/keijiban_mobile.html"
        else:
            template_name = "bbs/keijiban_pc.html"
        # if self.request.user.is_superuser:
        #     template_name = 'bbs/template_superuser.html'
        # elif self.request.user.is_authenticated:
        #     template_name = 'bbs/template_authenticated.html'
        # else:
        #     template_name = self.template_name
        return [template_name]

    def get_context_data(self, **kwargs):
        """有効な画像を表示する"""
        context = super().get_context_data(**kwargs)
        css = self.request.GET.get("css", "contain")
        qs = File.objects.filter(alive=True).order_by("-created_at")
        max_date = File.objects.filter(alive=True).aggregate(Max("created_at"))

        # formフィールドに初期値を設定。
        selectcssform = SwitchCSSForm(
            initial={
                "css": css,
            }
        )
        # 最新の画像データ登録日をタイトル表示させる。
        context["title"] = max_date["created_at__max"]
        context["file_list"] = qs
        context["form"] = selectcssform
        context["css"] = css
        return context


def expandView(request, pk):
    """拡大イメージを表示
    非常にシンプルなので、関数としてみる。
    """
    img_obj = File.objects.get(pk=pk)
    context = {"img_obj": img_obj}
    return render(request, "bbs/file_expand.html", context)
