from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .filters import DirectoryFilter
from .models import Directory
from .serializers import DirectorySerializer


class DirectoryAPIView(ListModelMixin, GenericViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DirectoryFilter

