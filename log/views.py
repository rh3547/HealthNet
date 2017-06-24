"""
HealthNet Log Views
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *
from .models import *
from profiles.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
import time


def logForm(request):
    if request.method == 'POST':

        try:
            logEvents = LogEvent.objects.all()
        except:
            logEvents = None

        try:
            if request.POST['source'] != "":
                logEvents = logEvents.filter(source=request.POST['source'])
            if request.POST['action'] != "":
                logEvents = logEvents.filter(action=request.POST['action'])
            if request.POST['eventCode'] != "":
                logEvents = logEvents.filter(eventCode=request.POST['eventCode'])
            if request.POST['date'] != "":
                logEvents = logEvents.filter(date=request.POST['date'])
            if request.POST['time'] != "":
                logEvents = logEvents.filter(time=request.POST['time'])
        except:
            logEvents = None

        try:
            logEvents = logEvents.order_by('-date')
        except:
            logEvents = None

        return render(request, 'log/loglist.html', {'logEvents': logEvents})

    else:
        form = LogForm()
        return render(request, 'log/logform.html', {'form': form})


def logDelete(request, pk):
    log = LogEvent.objects.get(pk=pk)
    log.delete()
    return HttpResponseRedirect("/log")


def createLogEvent(source, action, eventCode, message):
    log = LogEvent()
    log.source = source
    log.action = action
    log.eventCode = eventCode
    log.date = time.strftime("%Y-%m-%d")
    log.time = time.strftime("%I:%M %p")
    log.message = message
    log.save()
