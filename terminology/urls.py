from django.urls import path
from rest_framework import routers

from .views import DirectoryAPIView,  ItemsAPIView

router = routers.DefaultRouter()
router.register("directories", DirectoryAPIView)

urlpatterns = router.urls

urlpatterns += [
    path("directories/<int:pk>/items", ItemsAPIView.as_view({"get": "list"})),
    path("directories/<int:pk>/items/validate", ItemsAPIView.as_view({"post": "validate"}))
]
