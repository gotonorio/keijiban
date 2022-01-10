from bbs.models import File
from django.views import generic


class KeijiFileListView(generic.ListView):
    """ 掲示板list一覧 """
    model = File
    template_name = "bbs/file_list.html"
    queryset = File.objects.all().order_by('-created_at')
