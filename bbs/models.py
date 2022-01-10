import os

from django.db import models
from django.utils import timezone


class Category(models.Model):
    """ カテゴリ """
    name = models.CharField(verbose_name='カテゴリ', max_length=32)
    path_name = models.CharField(verbose_name='パス名', max_length=128)
    rank = models.IntegerField(verbose_name='表示順', default=0)
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)
    restrict = models.BooleanField(verbose_name='制限', default=False)
    alive = models.BooleanField(verbose_name='有効', default=True)

    def __str__(self):
        return self.name


def get_upload_to(instance, filename):
    """ upload_toを動的(カテゴリのpath毎)に指定する
    https://docs.djangoproject.com/ja/4.0/ref/models/fields/
    ここで、ファイルをuploadするパスを設定する。
    media/カテゴリのpath/filename
    """
    try:
        path = os.path.join(str(instance.category.path_name), filename)
    except Exception as e:
        _ = e
        path = os.path.join('default', filename)
    return path


class File(models.Model):
    """ アップロードするファイル """
    title = models.CharField(verbose_name='タイトル', max_length=32)
    summary = models.TextField(verbose_name='概要', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ',
                                 on_delete=models.PROTECT, null=True, blank=True)
    src = models.FileField(verbose_name='FilePath', upload_to=get_upload_to)
    rank = models.IntegerField(verbose_name='表示順', default=0)
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)
    alive = models.BooleanField(verbose_name='有効', default=True)

    def __str__(self):
        return self.title

    def get_filename(self):
        """ ファイル名を返す """
        return os.path.basename(self.src.name)
