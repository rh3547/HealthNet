"""
HealthNet Profile Views
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from .validate import *
from .forms import *
from .models import *
from log.models import LogEvent
from log.views import createLogEvent
import time

# The index view simply renders the index.html template with a blank login form.
def index(request):
    form = IndexForm()

    if request.method == 'POST':
        message = request.POST['error_message']
        return render(request, 'profiles/index.html', {'form': form, 'error_message': message})
    else:
        return render(request, 'profiles/index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        authUser = User()

        try:
            authUser.username = validateUser(request.POST['username'])
        except InvalidInput as ii:
            messages.add_message(request, messages.INFO, ii.args[0])
            createLogEvent("n/a", "view: register", 1, "Tried to register with an existing username")
            return HttpResponseRedirect("/")

        try:
            authUser.email = validateEmail(request.POST['email'])
        except InvalidInput as ii:
            messages.add_message(request, messages.INFO, ii.args[0])
            createLogEvent("n/a", "view: register", 1, "Given email failed validation")
            return HttpResponseRedirect("/")

        try:
            authUser.set_password(validatePass(request.POST['password']))
        except InvalidInput as ii:
            messages.add_message(request, messages.INFO, ii.args[0])
            createLogEvent("n/a", "view: register", 1, "Given password failed validation")
            return HttpResponseRedirect("/")

        authUser.first_name = ""
        authUser.last_name = ""
        authUser.is_active = True
        authUser.is_staff = False
        authUser.is_superuser = False
        authUser.save()

        newUser = Patient()
        newUser.user = authUser
        newUser.isNew = True
        newUser.accountType = 'P'
        newUser.birthDate = "1993-08-21"
        newUser.heightFeet = 5
        newUser.heightInches = 11
        newUser.weight = 150
        newUser.insuranceCompany = ""
        newUser.insuranceId = ""
        newUser.allergies = "None"
        newUser.conditions = "None"
        newUser.prescriptions = "None"
        newUser.hospitalPref = ""
        newUser.save()

        createLogEvent(request.POST['username'], "view: register", 0, "Successful registration")

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        auth_login(request, user)

        patientForm = NewPatientForm()
        contactForm = UserContactForm()
        return render(request, 'profiles/newpatient.html',
                      {'username': request.POST['username'], 'patientForm': patientForm, 'contactForm': contactForm})


# The login view takes the form data from the index view and uses it to authenticate
# and log in a user.
def login(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        # The password verified for the user
        if user.check_password(request.POST['password']):
            if user.is_active:
                auth_login(request, user)

                createLogEvent(request.POST['username'], "view: login", 2, "Successful login")

                user = User.objects.get(username=request.user.username).healthnetuser

                if user.isNew:
                    patientForm = NewPatientForm()
                    contactForm = UserContactForm()
                    return render(request, 'profiles/newpatient.html',
                                  {'username': request.POST['username'], 'patientForm': patientForm,
                                   'contactForm': contactForm})
                else:
                    return HttpResponseRedirect("/profiles/" + request.POST['username'])
            else:
                message = "This account has been disabled."
                messages.add_message(request, messages.INFO, message)
                createLogEvent(request.POST['username'], "view: login", 3, "The account trying to be accessed has been disabled")
                return HttpResponseRedirect("/")
        else:
            message = "Incorrect password..."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.POST['username'], "view: login", 3, "Input wrong password for the given account")
            return HttpResponseRedirect("/")
    else:
        # The authentication system was unable to verify the username and password
        message = "Username and/or password not recognized!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent(request.POST['username'], "view: login", 3, "Given credentials not recognized by system")
        return HttpResponseRedirect("/")


def logout(request):
    createLogEvent(request.user.username, "view: logout", 4, "User logged out")
    auth_logout(request)
    message = "Successfully logged out!"
    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect("/")


# The viewProfile view obtains the user by userName and displays that user's information.
def viewProfile(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:
            hnuser = User.objects.get(username=username).healthnetuser

            if hnuser.accountType == 'P':
                hnuser = hnuser.patient

                if request.method == 'POST':

                    contact = Contact()
                    contact.street = request.POST['street']
                    contact.city = request.POST['city']
                    contact.state = request.POST['state']
                    contact.zipcode = request.POST['zipcode']
                    contact.firstName = request.POST['firstName']
                    contact.lastName = request.POST['lastName']
                    contact.middleInitial = request.POST['middleInitial']
                    contact.phoneNumber = request.POST['phoneNumber']
                    contact.relation = 'se'
                    contact.healthnetuser = hnuser
                    contact.user_id = hnuser.pk
                    contact.save()

                    hnuser.birthDate = request.POST['birthDate']
                    hnuser.heightFeet = request.POST['heightFeet']
                    hnuser.heightInches = request.POST['heightInches']
                    hnuser.weight = request.POST['weight']
                    hnuser.insuranceCompany = request.POST['insuranceCompany']
                    hnuser.insuranceId = request.POST['insuranceId']
                    hnuser.hospitalPref = request.POST['hospitalPref']
                    hnuser.isNew = False
                    hnuser.save()

                    createLogEvent(request.user.username, username, 10, "User profile information was edited")

                    return HttpResponseRedirect("/profiles/" + username)
                else:
                    createLogEvent(request.user.username, username, 5, "User viewed a profile")
                    try:
                        contacts = Contact.objects.filter(user_id=hnuser.id).exclude(relation='se')
                        thiscontact = Contact.objects.get(relation='se', user_id=hnuser.id)
                    except (KeyError, Contact.DoesNotExist):
                        form = ContactForm()
                        return render(request, 'profiles/addcontact.html', {'form': form, 'username': username})
                    else:
                        return render(request, 'profiles/patientprofile.html',
                                      {'hnuser': hnuser, 'contacts': contacts, 'thiscontact': thiscontact})
            else:
                message = "Account type not yet implemented."
                messages.add_message(request, messages.INFO, message)
                return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 11, "User attempted to view a profile without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 11, "Someone attempted to view a profile without being logged in")
        return HttpResponseRedirect("/")

# The viewContacts view shows a list of all a user's contacts.
def viewContacts(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:

            user = User.objects.get(username=request.user.username).healthnetuser.patient
            contacts = Contact.objects.filter(user_id=user.id).exclude(relation='se')

            createLogEvent(request.user.username, username, 6, "User viewed a list of contacts")

            return render(request, 'profiles/viewcontacts.html', {'username': username, 'hnuser': user, 'contacts': contacts})
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 11, "User attempted to view a user's contacts without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 11, "Someone attempted to view a user's contacts without being logged in")
        return HttpResponseRedirect("/")

# The addContact view presents a form to fill in that adds a new contact to the user.
def addContact(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:
            form = ContactForm(no_self=True)

            if request.method == 'POST':
                contact = Contact()
                contact.street = request.POST['street']
                contact.city = request.POST['city']
                contact.state = request.POST['state']
                contact.zipcode = request.POST['zipcode']
                contact.firstName = request.POST['firstName']
                contact.lastName = request.POST['lastName']
                contact.middleInitial = request.POST['middleInitial']
                contact.phoneNumber = request.POST['phoneNumber']
                contact.relation = request.POST['relation']
                contact.healthnetuser = User.objects.get(username=request.user.username).healthnetuser
                contact.user_id = User.objects.get(username=username).healthnetuser.pk
                contact.save()

                createLogEvent(request.user.username, username, 7, "User added a new contact")

                return HttpResponseRedirect("/profiles/" + username + "/contacts")
            else:
                user = User.objects.get(username=request.user.username).healthnetuser.patient
                return render(request, 'profiles/addcontact.html', {'form': form, 'username': username, 'hnuser': user})
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 13, "User attempted to create a user contact without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 13, "Someone attempted to create a user contact without being logged in")
        return HttpResponseRedirect("/")


def editContact(request, username, pk):
    if request.user.is_authenticated():
        if request.user.username == username:
            contact = Contact.objects.get(pk=pk)
            if contact.user_id == User.objects.get(username=request.user.username).healthnetuser.pk:
                if request.method == 'POST':
                    contact.street = request.POST['street']
                    contact.city = request.POST['city']
                    contact.state = request.POST['state']
                    contact.zipcode = request.POST['zipcode']
                    contact.firstName = request.POST['firstName']
                    contact.lastName = request.POST['lastName']
                    contact.middleInitial = request.POST['middleInitial']
                    contact.phoneNumber = request.POST['phoneNumber']
                    contact.relation = request.POST['relation']
                    contact.save()

                    createLogEvent(request.user.username, username, 8, "User edited a contact")

                    return HttpResponseRedirect("/profiles/" + username)
                else:
                    data = {
                        'street': contact.street,
                        'city': contact.city,
                        'state': contact.state,
                        'zipcode': contact.zipcode,
                        'firstName': contact.firstName,
                        'lastName': contact.lastName,
                        'middleInitial': contact.middleInitial,
                        'phoneNumber': contact.phoneNumber,
                        'relation': contact.relation,
                    }
                    form = ContactForm(data, no_self=True)
                    user = User.objects.get(username=request.user.username).healthnetuser.patient
                    return render(request, 'profiles/editcontact.html',
                                  {'form': form, 'username': username, 'pk': pk, 'hnuser': user})
            else:
                message = "You do not have permission to view the requested page."
                messages.add_message(request, messages.INFO, message)
                createLogEvent(request.user.username, username, 12, "User attempted to edit a user contact without permission")
                return HttpResponseRedirect("/")

        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 12, "User attempted to edit a user contact without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 12, "Someone attempted to edit a user contact without being logged in")
        return HttpResponseRedirect("/")


def deleteContact(request, username, pk):
    if request.user.is_authenticated():
        if request.user.username == username:
            contact = Contact.objects.get(pk=pk)
            if contact.user_id == User.objects.get(username=request.user.username).healthnetuser.pk:
                contactName = contact.firstName
                contact.delete()
                message = "Contact \'" + contactName + "\' successfully deleted."
                messages.add_message(request, messages.INFO, message)
                createLogEvent(request.user.username, username, 9, "User deleted a contact")
                return HttpResponseRedirect("/profiles/" + username + "/contacts")
            else:
                message = "You do not have permission to do that."
                messages.add_message(request, messages.INFO, message)
                createLogEvent(request.user.username, username, 14, "User attempted to delete a user contact without permission")
                return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to do that."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 14, "User attempted to delete a user contact without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 14, "Someone attempted to delete a user contact without being logged in")
        return HttpResponseRedirect("/")


def editProfile(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:
            user = User.objects.get(username=username).healthnetuser

            if user.accountType == 'P':
                if request.method == 'POST':
                    patient = Patient.objects.get(healthnetuser_ptr=user)
                    form = EditPatientForm(request.POST, instance=patient)
                    form.save()
                    return HttpResponseRedirect("/profiles/" + username)
                else:
                    patient = Patient.objects.get(healthnetuser_ptr=user)
                    birthDate = patient.birthDate
                    form = EditPatientForm(instance=patient)
                    return render(request, 'profiles/editpatientprofile.html',
                                  {'form': form, 'username': username, 'hnuser': user, 'birthDate': birthDate})

                createLogEvent(request.user.username, username, 10, "User edited profile information")
            else:
                message = "Account type not yet implemented."
                messages.add_message(request, messages.INFO, message)
                return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 12, "User attempted to edit a profile without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 12, "Someone attempted to edit a profile without being logged in")
        return HttpResponseRedirect("/")


# The view is temporary.  It is used to test new UI features.
def uiTest(request):
    return render(request, 'profiles/../appointments/templates/calendartest.html')

# AUTHENTICATION TEMPLATE
# if request.user.is_authenticated():
#     if request.user.username == username:
#         # User is successfully authenticated and logged in
#         # Do stuff...
#     else:
#         message = "You do not have permission to view the requested page."
#         messages.add_message(request, messages.INFO, message)
#         return HttpResponseRedirect("/")
# else:
#     message = "You must login to do that!"
#     messages.add_message(request, messages.INFO, message)
#     return HttpResponseRedirect("/")
