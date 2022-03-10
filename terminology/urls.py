from django.urls import path
from rest_framework import routers

from .views import DirectoryAPIView, ActualItemsAPIView, ItemsAPIView

router = routers.DefaultRouter()
router.register("directories", DirectoryAPIView)

urlpatterns = router.urls

urlpatterns += [
    path("directories/<int:pk>/actual", ActualItemsAPIView.as_view({"get": "list"})),
    path("directories/<int:pk>/all", ItemsAPIView.as_view({"get": "list"}))
]