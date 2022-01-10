from bbs.models import File
from django.views import generic


class KeijibanView(generic.ListView):
    """ 掲示板表示 """
    model = File
    template_name = "bbs/keijiban.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        qs = qs.filter(alive=True).order_by('created_at')
        return qs
