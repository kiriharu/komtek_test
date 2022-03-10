import operator
from datetime import date
from functools import reduce
from typing import Optional

from django.db.models import QuerySet, Subquery, Q

from terminology.models import Item, DirectoryVersion


def get_actual_directory_items(pk: Optional[int]) -> QuerySet[Item]:
    """
    Получает элементы заданного справочника текущей версии,
    на основе времени начала действия
    """
    # получаем текущую версию справочника на данный момент времени
    directory = DirectoryVersion.objects.filter(
        directory_id=pk,
        start_date__lte=date.today()
    ).order_by(
        "-start_date"
    )
    # достаем все элементы связанные с данной версией справочника
    return Item.objects.filter(
        directory_version_id=Subquery(queryset=directory.values("pk")[:1])
    )


def get_items_related_to_directory(pk: Optional[int]) -> QuerySet[Item]:
    """
    Получает элементы заданного справочника
    """
    return Item.objects.filter(
        directory_version__directory_id=pk
    )


def filter_unexpected_items(queryset: QuerySet, values: list[dict]) -> QuerySet[Item]:
    """
    Фильтрует неизвестные элементы, возвращает только те, которые есть в указанном каталоге
    """
    return queryset.filter(reduce(operator.or_, [
        Q(code=item.get('code'),
          value=item.get('value'),
          parent=item.get('parent'))
        for item in values
    ]))
