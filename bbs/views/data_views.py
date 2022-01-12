from bbs.forms import FileForm
from bbs.models import File
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from PIL import Image


class FileCreateView(PermissionRequiredMixin, generic.CreateView):
    """ 管理者用 ファイルの作成. """
    model = File
    form_class = FileForm
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_list')


class FileUpdateView(PermissionRequiredMixin, generic.UpdateView):
    """ 管理者用 ファイルの更新. """
    model = File
    form_class = FileForm
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_list')


class FileDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """ 管理者用 ファイルの削除. """
    template_name = 'bbs/file_confirm_delete.html'
    model = File
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_list')


class FileListView(PermissionRequiredMixin, generic.ListView):
    """ 掲示板list一覧 """
    model = File
    template_name = "bbs/file_list.html"
    permission_required = ("bbs.add_file")

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        qs = qs.filter(alive=True).order_by('created_at')
        return qs


class FileRotateView(PermissionRequiredMixin, generic.TemplateView):
    """ 写真の回転処理
    イメージを読み込んで、時計回りに90度回転して保存する。
    """
    permission_required = ("bbs.add_file")
    template_name = "bbs/file_rotate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # imageのurlを求める
        qs = File.objects.get(pk=pk)
        img_url = qs.img.url
        # ToDo:行頭の/が余計？行頭の1文字を削除すると問題ないようだ。
        img_url = img_url[1:]
        img = Image.open(img_url)
        img_rotate = img.rotate(-90, expand=True)
        img_rotate.save(img_url)
        qs = File.objects.get(pk=pk)
        context['img'] = qs.img.url
        return context
