from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .filters import DirectoryFilter
from .models import Directory
from .serializers import DirectorySerializer, ItemSerializer
from .services import get_actual_directory_items


class DirectoryAPIView(ListModelMixin, GenericViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DirectoryFilter


class ActualItemsAPIView(ListModelMixin, GenericViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return get_actual_directory_items(self.kwargs.get("pk", None))

