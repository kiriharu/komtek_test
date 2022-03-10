from datetime import date
from typing import Optional

from django.db.models import QuerySet, Subquery

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
