"""
HealthNet appointments Forms
"""
from django import forms

from .models import Appointment

class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('title', 'doctor', 'hospital', 'room', 'reason')
        labels = {
            'title': 'Title',
            'doctor': 'Doctor',
            'hospital': 'Hospital',
            'room': 'Room',
            'reason': 'Reason'
        }
