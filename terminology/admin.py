from django.contrib import admin
from django.template.defaultfilters import truncatewords

from .models import Directory, DirectoryVersion, Item


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "short_name", "short_desc", )
    list_display_links = ("name", )
    search_fields = ("name", "short_name", "description", )

    @admin.display(description="Описание")
    def short_desc(self, obj):
        """
        Описание справочника, порезанное на 10 символов
        """
        return truncatewords(obj.description, 10)


@admin.register(DirectoryVersion)
class DirectoryVersionAdmin(admin.ModelAdmin):

    list_display = ("id", "directory", "version", "start_date", )
    list_display_links = ("version", )
    search_fields = ("version", "directory__name")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id", "parent", "code", "value",
        "directory_version",
    )
    search_fields = ("code", "value")
