import django_filters

from .models import Directory


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
