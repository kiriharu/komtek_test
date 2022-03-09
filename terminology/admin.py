from django.contrib import admin

from .models import Directory, DirectoryVersion, Item


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectoryVersion)
class DirectoryVersionAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
