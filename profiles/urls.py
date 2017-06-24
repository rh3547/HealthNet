"""
HealthNet Profile URLs
"""
from django.conf.urls import url

from . import views

app_name = 'profiles'  # namespace

urlpatterns = [
    # The root URL links to the index view that displays the login page
    url(r'^$', views.index, name='index'),

    # The register URL links to the register view to create a new user
    url(r'^register/$', views.register, name='register'),

    # The login URL links to the login view which authenticates a user with the given form data
    url(r'^login/$', views.login, name='login'),

    # The logout URL links to the login view which simply logs out the current session
    url(r'^logout/$', views.logout, name='logout'),

    # This URL links to the viewProfile view that displays a user's information
    url(r'^profiles/(?P<username>\w*)$', views.viewProfile, name='viewProfile'),

    # This URL links to the addContact view which presents a form to add a new user contact
    url(r'^profiles/(?P<username>\w+)/addcontact$', views.addContact, name='addContact'),

    # This URL links to the viewContacts view which shows a list of all the user's contacts
    url(r'^profiles/(?P<username>\w+)/contacts$', views.viewContacts, name='viewContacts'),

    # This URL links to the editContact view which presents a form to edit their contacts
    url(r'^profiles/(?P<username>\w+)/editcontact/(?P<pk>[0-9]+)$', views.editContact, name='editContact'),

    # This URL links to the deleteContact view which deletes the contact
    url(r'^profiles/(?P<username>\w+)/deletecontact/(?P<pk>[0-9]+)$', views.deleteContact, name='deleteContact'),

    # This URL links to the editProfile view which presents a form to edit profile information
    url(r'^profiles/(?P<username>\w+)/edit$', views.editProfile, name="editProfile"),

    # This is a temporary URL used to test new UI features
    url(r'^ui$', views.uiTest, name="uiTest"),
]
