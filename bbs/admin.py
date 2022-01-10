from django.contrib import admin
from bbs.models import Category, File


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'created_at')


admin.site.register(Category, CategoryAdmin)


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank', 'created_at')


admin.site.register(File, FileAdmin)