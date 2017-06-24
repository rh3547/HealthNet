"""
HealthNet Log urls
"""

from django.conf.urls import url

from . import views

app_name = 'log'  # namespace

urlpatterns = [

    # The URL to the log form and log view
    url(r'^$', views.logForm, name='logForm'),

    # This URL will delete a log event with the given primary key
    url(r'^(?P<pk>[0-9]+)/delete$', views.logDelete, name='logDelete'),

    # The URL to parse a specific log request
    # url(r'^(?P<query>\w+)$', views.logParse, name='logParse'),

]
