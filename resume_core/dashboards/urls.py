# from django.urls import path
from rest_framework.routers import SimpleRouter

from .views.dashboard import DashboardViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'dashboards', DashboardViewSet)

urlpatterns = router.urls
