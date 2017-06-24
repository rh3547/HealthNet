"""
HealthNet Appointments urls
"""

from django.conf.urls import url

from . import views

app_name = 'appointments'  # namespace

urlpatterns = [
    # The URL to create an appointment
    url(r'^(?P<username>\w+)/createappointment$', views.createAppointment, name='createAppointment'),

    url(r'^(?P<username>\w+)/(?P<pk>[0-9]+)$', views.viewAppointment, name='viewAppointment'),

    url(r'^(?P<username>\w+)/(?P<pk>[0-9]+)/edit$', views.editAppointment, name='editAppointment'),

    url(r'^(?P<username>\w+)/(?P<pk>[0-9]+)/cancel$', views.cancelAppointment, name='cancelAppointment'),

    url(r'^(?P<username>\w+)$', views.viewCalendar, name='viewCalendar'),

    url(r'^ui$', views.uiTest, name='uiTest'),

]
