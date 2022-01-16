from bbs.models import File
from django.shortcuts import render
from django.views import generic
from django.db.models.aggregates import Max
import logging


class KeijibanView(generic.ListView):
    """ 掲示板表示 """
    model = File
    template_name = "bbs/keijiban.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        qs = qs.filter(alive=True).order_by('created_at')
        return qs

    def get_context_data(self, **kwargs):
        """ 最新の日付データをタイトルとして表示する """
        context = super().get_context_data(**kwargs)
        qs = File.objects.filter(alive=True).aggregate(Max('created_at'))
        tz = qs['created_at__max'] 
        logging.debug(tz)
        context["title"] = tz
        return context
    

def expandView(request, pk):
    """ 拡大イメージを表示
    非常にシンプルなので、関数としてみる。
    """
    img_obj = File.objects.get(pk=pk)
    context = {'img_obj': img_obj}
    return render(request, 'bbs/file_expand.html', context)
