from rest_framework.routers import DefaultRouter

from .views import AirplaneViewSet

router = DefaultRouter()
router.register("", AirplaneViewSet, basename="airplanes")

urlpatterns = router.urls
