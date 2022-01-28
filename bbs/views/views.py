from bbs.forms import SwitchCSSForm
from bbs.models import File
from django.db.models.aggregates import Max
from django.shortcuts import render
from django.views import generic


class KeijibanView(generic.TemplateView):
    """ 掲示板表示 """
    model = File
    template_name = "bbs/keijiban.html"

    def get_template_names(self):
        """ templateファイルを切り替える """
        if self.request.user_agent_flag == 'mobile':
            template_name = "bbs/mobile_keijiban.html"
        else:
            template_name = "bbs/pc_keijiban.html"
        # if self.request.user.is_superuser:
        #     template_name = 'bbs/template_superuser.html'
        # elif self.request.user.is_authenticated:
        #     template_name = 'bbs/template_authenticated.html'
        # else:
        #     template_name = self.template_name
        return [template_name]

    def get_context_data(self, **kwargs):
        """ 最新の日付データをタイトルとして表示する """
        context = super().get_context_data(**kwargs)
        css = self.request.GET.get('css', 'cover')
        qs = File.objects.filter(alive=True).order_by('-created_at')
        max_date = File.objects.filter(alive=True).aggregate(Max('created_at'))

        # formフィールドに初期値を設定。
        selectcssform = SwitchCSSForm(initial={
            'css': css,
        })

        context["title"] = max_date['created_at__max']
        context['file_list'] = qs
        context['form'] = selectcssform
        context['css'] = css
        return context


def expandView(request, pk):
    """ 拡大イメージを表示
    非常にシンプルなので、関数としてみる。
    """
    img_obj = File.objects.get(pk=pk)
    context = {'img_obj': img_obj}
    return render(request, 'bbs/file_expand.html', context)
