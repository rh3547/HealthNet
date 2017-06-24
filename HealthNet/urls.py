"""
HealthNet URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Route to the admin panel
    url(r'^admin/', include(admin.site.urls)),

    # Have the root URL route to the profiles app URLs
    url(r'^', include('profiles.urls')),

    # Have /appointments route to the appointments app URLs
    url(r'^appointments/', include('appointments.urls')),

    # Have /log route to the Log app URLs
    url(r'^log/', include('log.urls')),
]
