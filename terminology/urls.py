from rest_framework import routers

from .views import DirectoryAPIView
router = routers.DefaultRouter()
router.register("directories", DirectoryAPIView)

urlpatterns = router.urls
