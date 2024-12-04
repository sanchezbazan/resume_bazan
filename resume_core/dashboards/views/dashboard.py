from rest_framework import viewsets

from ..models.dashboard import Dashboard
from ..serializers.dashboard import DashboardReadSerializer


class DashboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing dashboards.
    """
    queryset = Dashboard.objects.all()
    serializer_class = DashboardReadSerializer


# class ListDashboard(generics.ListAPIView):
#     queryset = Dashboard.objects.all()
#     serializer_class = DashboardReadSerializer

# class DetailDashboard(generics.RetrieveAPIView):
#     queryset = Dashboard.objects.all()
#     serializer_class = DashboardReadSerializer
