import os

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def get_upload_to(instance, filename):
    """ upload_toを動的(カテゴリのpath毎)に指定する
    https://docs.djangoproject.com/ja/4.0/ref/models/fields/
    ここで、ファイルをuploadするパスを設定する。
    media/カテゴリのpath/filename
    """
    try:
        path = os.path.join(settings.IMAGE_PATH, filename)
    except Exception as e:
        _ = e
        path = os.path.join('default', filename)
    return path


def image_size(value):
    """ アップロード写真のサイズを制限 """
    limit = settings.LIMMIT_IMAGE_SIZE
    if value.size > limit:
        raise ValidationError(f'ファイルサイズは {limit} byte以下にしてください。')


class File(models.Model):
    """ アップロードするイメージファイル """
    title = models.CharField(verbose_name='タイトル', max_length=32)
    summary = models.CharField(verbose_name='概要', max_length=128, blank=True, null=True)
    img = models.ImageField(verbose_name='写真ファイル', upload_to=get_upload_to,
                            validators=[image_size], null=True, blank=True)
    rank = models.IntegerField(verbose_name='表示順', default=0)
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)
    alive = models.BooleanField(verbose_name='有効', default=True)

    def __str__(self):
        return self.title
