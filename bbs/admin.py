from django.contrib import admin
from bbs.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank', 'created_at')


admin.site.register(File, FileAdmin)
