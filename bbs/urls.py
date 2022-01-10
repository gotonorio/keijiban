from django.urls import path
from bbs.views import views
from bbs.views import data_views


app_name = 'bbs'
urlpatterns = [
    path('', views.KeijiFileListView.as_view(), name='list'),
    path('list/', views.KeijiFileListView.as_view(), name='list'),
    # ファイル登録・修正
    path('file/create/<int:pk>', data_views.FileCreateView.as_view(), name='file_create'),
    path('file/update/<int:pk>', data_views.FileUpdateView.as_view(), name='file_update'),
    path('file/delete/<int:pk>', data_views.FileDeleteView.as_view(), name='file_delete'),
]
