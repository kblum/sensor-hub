from django.contrib import admin
from .models import Location, Deployment, Sensor, Reading, Token, UserAgent


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
    list_display = ('id', 'sensor', 'deployment', 'temperature', 'user_agent', 'created', 'modified',)
    list_filter = ('sensor', 'deployment',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_key', 'api_secret', 'enabled', 'created', 'modified',)
    list_filter = ('enabled',)


class UserAgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_agent_string',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(UserAgent, UserAgentAdmin)
