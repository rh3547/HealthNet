from django.contrib import admin

from .models import LogEvent

class LogEventAdmin(admin.ModelAdmin):
    search_fields = ['action', 'source', 'eventCode']

admin.site.register(LogEvent, LogEventAdmin)
