from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .filters import DirectoryFilter, ItemFilter
from .models import Directory, Item
from .serializers import DirectorySerializer, ItemSerializer
from .services import get_actual_directory_items, get_items_related_to_directory


class DirectoryAPIView(ListModelMixin, GenericViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DirectoryFilter


class ActualItemsAPIView(ListModelMixin, GenericViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return get_actual_directory_items(self.kwargs.get("pk", None))


class ItemsAPIView(ListModelMixin, GenericViewSet):
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ItemFilter

    def get_queryset(self):
        return get_items_related_to_directory(self.kwargs.get("pk", None))

