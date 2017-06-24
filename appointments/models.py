"""
HealthNet Appointments models
"""

from django.db import models
from profiles.models import Patient


class Appointment(models.Model):
    title = models.CharField(max_length=32)
    startDate = models.DateField()
    startTime = models.CharField(max_length=10)
    endDate = models.DateField()
    endTime = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient)
    doctor = models.CharField(max_length=96)
    hospital = models.CharField(max_length=64)
    room = models.CharField(max_length=32)
    reason = models.TextField();

    def startHours(self):
        splox = self.startTime.split(':')
        splox[0] = int(splox[0])
        if (splox[1][-2:].upper()=='PM'):
            splox[0] += 12
        return splox[0]

    def startMinutes(self):
        splox = self.startTime.split(':')
        splox[0] = int(splox[0])
        splox[1] = int(splox[1][:-2])
        return splox[1]

    def endHours(self):
        splox = self.endTime.split(':')
        splox[0] = int(splox[0])
        if (splox[1][-2:].upper()=='PM'):
            splox[0] += 12
        return splox[0]

    def endMinutes(self):
        splox = self.endTime.split(':')
        splox[0] = int(splox[0])
        splox[1] = int(splox[1][:-2])
        return splox[1]

    def __str__(self):
        return self.title
