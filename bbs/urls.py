from django.urls import path
from bbs.views import views
from bbs.views import data_views


app_name = 'bbs'
urlpatterns = [
    path('', views.KeijibanView.as_view(), name='list'),
    path('list/', views.KeijibanView.as_view(), name='list'),
    path('bbs/expand/<int:pk>', views.expandView, name='file_expand'),
    # ファイル登録・修正
    path('bbs/list/', data_views.FileListView.as_view(), name='file_list'),
    path('bbs/create/', data_views.FileCreateView.as_view(), name='file_create'),
    path('bbs/update/<int:pk>', data_views.FileUpdateView.as_view(), name='file_update'),
    path('bbs/delete/<int:pk>', data_views.FileDeleteView.as_view(), name='file_delete'),
    path('bbs/rotate/<int:pk> <int:direc>', data_views.FileRotateView.as_view(), name='file_rotate'),
]
