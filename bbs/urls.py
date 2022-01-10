from django.urls import path
from bbs.views import views
from bbs.views import data_views


app_name = 'bbs'
urlpatterns = [
    path('', views.KeijiFileListView.as_view(), name='list'),
    path('list/', views.KeijiFileListView.as_view(), name='list'),
    # ファイル登録・修正
]
