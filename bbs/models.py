import os
from io import BytesIO

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import models
from django.utils import timezone
from PIL import Image

user = get_user_model()


def get_upload_to(instance, filename):
    """upload_toを動的(カテゴリのpath毎)に指定する
    https://docs.djangoproject.com/ja/4.0/ref/models/fields/
    ここで、ファイルをuploadするパスを設定する。
    settings.pyで設定したMEDIA_ROOT + IMAGE_PATH + filenameとなる。
    """
    try:
        path = os.path.join(settings.IMAGE_PATH, filename)
    except Exception as e:
        _ = e
        path = os.path.join("default", filename)
    return path


def image_size(value):
    """アップロード写真のサイズを制限"""
    limit_kb = settings.LIMMIT_IMAGE_SIZE
    if value.size > limit_kb * 1024:
        raise ValidationError(f"ファイルサイズは {limit_kb}KB 以下にしてください。")
    # if value.size > limit:
    #     mb = limit / 1024 / 1024
    #     raise ValidationError(f"ファイルサイズは {mb}MB 以下にしてください。")


def remove_exif(image_field):
    """exifデータを削除する"""
    image = Image.open(image_field)

    # 画像データを取得
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    # バッファに新しい画像を保存
    buffer = BytesIO()
    image_without_exif.save(buffer, format=image.format)
    buffer.seek(0)

    # ContentFileに変換して新しいファイルを作成
    return ContentFile(buffer.read())


class File(models.Model):
    """アップロードするイメージファイル"""

    title = models.CharField(verbose_name="タイトル", max_length=32)
    summary = models.CharField(verbose_name="概要", max_length=128, blank=True, null=True)
    img = models.ImageField(
        verbose_name="写真ファイル", upload_to=get_upload_to, validators=[image_size], null=True, blank=False
    )
    rank = models.IntegerField(verbose_name="表示順", default=0)
    user = models.ForeignKey(user, verbose_name="名前", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="作成日", default=timezone.now)
    alive = models.BooleanField(verbose_name="有効", default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """exifデータ消去"""
        if self.img:
            # EXIFデータを削除した画像を取得
            new_image = remove_exif(self.img)

            # 画像フィールドを新しいファイルに置き換える
            self.img.save(self.img.name, new_image, save=False)

        # 通常の保存を実行
        super().save(*args, **kwargs)
