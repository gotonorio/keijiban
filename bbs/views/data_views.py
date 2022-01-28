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

    def form_valid(self, form):
        # commitを停止する。
        self.object = form.save(commit=False)
        # userをセット。
        self.object.user = self.request.user
        # データを保存。
        self.object.save()
        return super().form_valid(form)


class FileUpdateView(PermissionRequiredMixin, generic.UpdateView):
    """ 管理者用 ファイルの更新. """
    model = File
    form_class = FileForm
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_list')

    def form_valid(self, form):
        # commitを停止する。
        self.object = form.save(commit=False)
        # userをセット。
        self.object.user = self.request.user
        # データを保存。
        self.object.save()
        return super().form_valid(form)


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
        qs = qs.filter(alive=True).order_by('-created_at')
        return qs


class FileRotateView(PermissionRequiredMixin, generic.TemplateView):
    """ 写真の回転処理
    iPhoneで写真が横向きになるため、修正の処理。
    イメージを読み込んで、時計回りに90度回転して保存する。
    https://docs.djangoproject.com/ja/4.0/topics/files/
    """
    permission_required = ("bbs.add_file")
    template_name = "bbs/file_rotate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        direc = self.kwargs['direc']
        # imageをpillowで読み込み、回転、保存する。
        qs = File.objects.get(pk=pk)
        img_path = qs.img.path
        img = Image.open(img_path)
        if direc == 1:
            img_rotate = img.rotate(270, expand=True)
        elif direc == 0:
            img_rotate = img.rotate(90, expand=True)
        img_rotate.save(img_path)
        qs = File.objects.get(pk=pk)
        context['img'] = qs.img.url
        return context
