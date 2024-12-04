from rest_framework import serializers

from ..models.dashboard import Dashboard


class DashboardReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dashboard
        fields = '__all__'
