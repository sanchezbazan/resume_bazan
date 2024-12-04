from django.contrib import admin

from .models.dashboard import Dashboard


class DashboardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'graph_type',
    )


admin.site.register(Dashboard, DashboardAdmin)
