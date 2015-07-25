from django.contrib import admin
from .models import Location, Deployment, Sensor, Reading


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'created', 'modified',)
    list_filter = ('enabled',)


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'enabled', 'created', 'modified',)
    list_filter = ('enabled', 'location')


class SensorAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'deployment', 'enabled', 'created', 'modified',)
    list_filter = ('enabled', 'deployment',)


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'deployment', 'temperature', 'created',)
    list_filter = ('sensor', 'deployment',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Reading, ReadingAdmin)
