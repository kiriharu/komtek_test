import django_filters
from django.db.models import QuerySet

from .models import Directory, Item, DirectoryVersion


class DirectoryFilter(django_filters.FilterSet):
    """ Фильтр для справочников """

    start_date = django_filters.DateFilter(
        field_name="versions__start_date",
        lookup_expr="lte",
        distinct="True"
    )

    class Meta:
        model = Directory
        fields = ("start_date", )


class ItemFilter(django_filters.FilterSet):

    version = django_filters.CharFilter(label="version", method="version_filter")

    def version_filter(
        self,
        queryset: QuerySet[Item],
        name: str,
        value: str
    ) -> QuerySet[Item]:
        """ Фильтрация элементов справочника по версии """
        # Находим версию
        version = DirectoryVersion.objects.filter(**{
            name: value,
            "directory": self.request.parser_context["kwargs"]["pk"]
        }).first()
        if version:
            return queryset.filter(directory_version=version)
        # Если ничего не нашли
        return queryset.none()
