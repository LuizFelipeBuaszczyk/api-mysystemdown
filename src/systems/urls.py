from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.routers import DefaultRouter

from systems.views.system_view import SystemViewSet
from systems.views.service_view import ServiceViewSet
from systems.views.bot_view import BotViewSet
from iam.views.membership_view import MembershipViewSet


router = DefaultRouter()
router.register(r"", SystemViewSet, basename="systems")

# router_pai, prefixo url pai, como você acessa o atributo central
nested = NestedDefaultRouter(router, "", lookup="system")
nested.register("memberships", MembershipViewSet, basename="system-memberships")
nested.register("services", ServiceViewSet, basename="system-services")
nested.register("bots", BotViewSet, basename="system-bots")

urlpatterns = router.urls + nested.urls