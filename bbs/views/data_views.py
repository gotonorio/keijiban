from bbs.forms import FileForm
from bbs.models import File
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic


class FileCreateView(PermissionRequiredMixin, generic.CreateView):
    """ 管理者用 ファイルの作成. """
    model = File
    form_class = FileForm
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_index')


class FileUpdateView(PermissionRequiredMixin, generic.UpdateView):
    """ 管理者用 ファイルの更新. """
    model = File
    form_class = FileForm
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_index')


class FileDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """ 管理者用 ファイルの削除. """
    template_name = 'bbs/file_confirm_delete.html'
    model = File
    # 必要な権限
    permission_required = ("bbs.add_file")
    # 権限がない場合、Forbidden 403を返す。これがない場合はログイン画面に飛ばす。
    raise_exception = True
    success_url = reverse_lazy('bbs:file_index')
