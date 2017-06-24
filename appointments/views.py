"""
HealthNet Appointments Views
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *
from .models import *
from profiles.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from log.views import createLogEvent
import json

# The create appointment view determines what type of accounbt is requesting
# to create an appointment, then sends the proper form and renders the proper
# template so the user can schedule a new appointment.

def createAppointment(request, username):
    if request.user.is_authenticated():
        hnuser = User.objects.get(username=username).healthnetuser

        if request.user.username == username:
            if request.method == 'POST':
                appointment = Appointment()

                appointment.title = request.POST['title']
                appointment.startDate = request.POST['startDate']
                appointment.startTime = request.POST['startTime']
                appointment.endDate = request.POST['endDate']
                appointment.endTime = request.POST['endTime']
                appointment.hospital = request.POST['hospital']
                appointment.room = request.POST['room']
                appointment.reason = request.POST['reason']

                if hnuser.accountType == 'P':
                    appointment.patient = hnuser.patient
                    appointment.doctor = request.POST['doctor']

                appointment.save()

                createLogEvent(request.user.username, username, 15, "User created appointment")

                return HttpResponseRedirect("/appointments/" + username)

            else:
                if hnuser.accountType == 'P':
                    template = 'appointments/createappointmentpatient.html'
                    form = PatientAppointmentForm()
                    hnuser = hnuser.patient

                return render(request, template, {'form': form, 'username': username, 'hnuser': hnuser})
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 13, "User attempted to create an appointment without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 13, "Someone attempted to create an appointment without being logged in")
        return HttpResponseRedirect("/")

def editAppointment(request, username, pk):
    if request.user.is_authenticated():
        hnuser = User.objects.get(username=username).healthnetuser
        appointment = Appointment.objects.get(pk=pk)

        if request.user.username == username:
            if hnuser.accountType == 'P':
                if appointment.patient == hnuser.patient:
                    if request.method == 'POST':
                        appointment.title = request.POST['title']
                        appointment.startDate = request.POST['startDate']
                        appointment.startTime = request.POST['startTime']
                        appointment.endDate = request.POST['endDate']
                        appointment.endTime = request.POST['endTime']
                        appointment.hospital = request.POST['hospital']
                        appointment.room = request.POST['room']
                        appointment.reason = request.POST['reason']
                        appointment.patient = hnuser.patient
                        appointment.doctor = request.POST['doctor']

                        appointment.save()

                        createLogEvent(request.user.username, username, 16, "User edited appointment")

                        return HttpResponseRedirect("/appointments/" + username + "/" + pk)

                    else:
                        startDate = appointment.startDate
                        startTime = appointment.startTime
                        endDate = appointment.endDate
                        endTime = appointment.endTime

                        if hnuser.accountType == 'P':
                            template = 'appointments/editappointmentpatient.html'
                            form = PatientAppointmentForm(instance=appointment)
                            hnuser = hnuser.patient

                        return render(request, template,
                                      {'form': form, 'appointment': appointment, 'startDate': startDate,
                                      'startTime': startTime, 'endDate': endDate, 'endTime': endTime,
                                      'username': username, 'pk': pk, 'hnuser': hnuser})
                else:
                    message = "You do not have permission to view the requested page."
                    messages.add_message(request, messages.INFO, message)
                    createLogEvent(request.user.username, username, 12, "User attempted to edit an appointment without permission")
                    return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 12, "User attempted to edit an appointment without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 12, "Someone attempted to edit an appointment without being logged in")
        return HttpResponseRedirect("/")

def viewAppointment(request, username, pk):
    if request.user.is_authenticated():
        hnuser = User.objects.get(username=username).healthnetuser
        appointment = Appointment.objects.get(pk=pk)
        patientContact = Contact.objects.get(relation='se', user=appointment.patient)

        if request.user.username == username:
            if hnuser.accountType == 'P':
                if appointment.patient == hnuser.patient:

                    createLogEvent(request.user.username, username, 19, "User viewed an appointment")

                    hnuser = hnuser.patient
                    return render(request, 'appointments/viewappointment.html', {'appointment': appointment, 'hnuser': hnuser, 'patientContact': patientContact})

                else:
                    message = "You do not have permission to view the requested page."
                    messages.add_message(request, messages.INFO, message)
                    createLogEvent(request.user.username, username, 11, "User attempted to view an appointment without permission")
                    return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 11, "User attempted to view an appointment without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 11, "Someone attempted to view an appointment without being logged in")
        return HttpResponseRedirect("/")

def cancelAppointment(request, username, pk):
    if request.user.is_authenticated():
        appointment = Appointment.objects.get(pk=pk)
        hnuser = User.objects.get(username=username).healthnetuser

        if request.user.username == username:
            if hnuser.accountType == 'P':
                if appointment.patient == hnuser.patient:
                    appointment.delete()

                    createLogEvent(request.user.username, username, 17, "User cancelled an appointment")
                    return HttpResponseRedirect("/appointments/" + username)
                else:
                    message = "You do not have permission to do that."
                    messages.add_message(request, messages.INFO, message)
                    createLogEvent(request.user.username, username, 14, "User attempted to cancel an appointment without permission")
                    return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to do that."
            messages.add_message(request, messages.INFO, message)
            createLogEvent(request.user.username, username, 14, "User attempted to cancel an appointment without permission")
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        createLogEvent("n/a", username, 14, "Someone attempted to cancel an appointment without being logged in")
        return HttpResponseRedirect("/")

# The view is temporary.  It is used to test new UI features.
def uiTest(request):
    return render(request, 'appointments/calendartest.html')

def viewCalendar(request, username):
    hnuser = User.objects.get(username=username).healthnetuser
    appointments = Appointment.objects.filter(patient=hnuser.patient)

    syears = {}
    smonths = {}
    sdays = {}
    shours = {}
    smins = {}
    eyears = {}
    emonths = {}
    edays = {}
    ehours = {}
    emins = {}
    ids = {}

    i = 0
    for appointment in appointments:
        syears[i] = appointment.startDate.year
        smonths[i] = appointment.startDate.month
        sdays[i] = appointment.startDate.day
        shours[i] = appointment.startHours()
        smins[i] = appointment.startMinutes()
        eyears[i] = appointment.endDate.year
        emonths[i] = appointment.endDate.month
        edays[i] = appointment.endDate.day
        ehours[i] = appointment.endHours()
        emins[i] = appointment.endMinutes()
        ids[i] = appointment.pk
        i += 1

    json_sy = json.dumps(syears)
    json_sm = json.dumps(smonths)
    json_sd = json.dumps(sdays)
    json_sh = json.dumps(shours)
    json_sn = json.dumps(smins)
    json_ey = json.dumps(eyears)
    json_em = json.dumps(emonths)
    json_ed = json.dumps(edays)
    json_eh = json.dumps(ehours)
    json_en = json.dumps(emins)
    json_id = json.dumps(ids)

    if (hnuser.accountType == 'P'):
        hnuser = hnuser.patient

    return render(request, 'appointments/calendartest.html', {'username': username,
                                                              'hnuser': hnuser,
                                                              'json_sy': json_sy,
                                                              'json_sm': json_sm,
                                                              'json_sd': json_sd,
                                                              'json_sh': json_sh,
                                                              'json_sn': json_sn,
                                                              'json_ey': json_ey,
                                                              'json_em': json_em,
                                                              'json_ed': json_ed,
                                                              'json_eh': json_eh,
                                                              'json_en': json_en,
                                                              'json_id': json_id,
                                                              'appointments': appointments})
