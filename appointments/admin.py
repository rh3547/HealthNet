from django.contrib import admin

from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['title', 'hospital', 'room', 'reason']}),
        ('Date/Time Info', {'fields': ['startDate', 'startTime', 'endDate', 'endTime']}),
        ('People Involved', {'fields': ['patient', 'doctor']}),
    ]

    search_fields = ['title']

admin.site.register(Appointment, AppointmentAdmin)
