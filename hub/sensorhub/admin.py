from django.contrib import admin
from .models import Location, Deployment, Sensor, Reading, Token


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enabled', 'created', 'modified',)
    list_filter = ('enabled',)


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'enabled', 'created', 'modified',)
    list_filter = ('enabled', 'location')


class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number', 'deployment', 'enabled', 'created', 'modified',)
    list_filter = ('enabled', 'deployment',)


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'deployment', 'temperature', 'created', 'modified',)
    list_filter = ('sensor', 'deployment',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_key', 'api_secret', 'enabled', 'created', 'modified',)
    list_filter = ('enabled',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Token, TokenAdmin)
