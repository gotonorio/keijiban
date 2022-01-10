from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.dispatch import receiver


class User(AbstractUser):
    """ デフォルトのUserを少し拡張してみる。
    管理画面でパスワード変更した時の日時を持たせる。
    パスワードを定期的に変更させる場合に使う。
    """
    update_password_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username

    def check_pw_date(self):
        return self.update_password_date


@receiver(models.signals.post_save, sender=User)
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    """ シグナルによってMyUserにgroupを追加する。
    https://stackoverflow.com/questions/51974276/how-to-automatically-add-group-and-staff-permissions-when-user-is-created/51975193
    """
    if created:
        try:
            group = Group.objects.get(name='guest')
        except ObjectDoesNotExist:
            pass
        else:
            instance.groups.add(group)
            instance.save()
