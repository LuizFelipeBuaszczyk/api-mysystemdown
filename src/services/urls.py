from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from services.views.service_view import ServiceViewSet
from services.views.request_view import RequestViewSet

router = DefaultRouter()
router.register(r"", ServiceViewSet, basename="services")

nested = NestedDefaultRouter(router, "", lookup="service")
nested.register("requests", RequestViewSet, basename="service-requests")

urlpatterns = router.urls + nested.urls