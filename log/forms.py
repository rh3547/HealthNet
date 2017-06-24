"""
HealthNet log Forms
"""
from django import forms

from .models import LogEvent

class LogForm(forms.ModelForm):
    class Meta:
        model = LogEvent
        fields = ('source', 'action', 'eventCode')
        labels = {
            'source': 'Log Source (What triggered the log event)',
            'action': 'Log Action (What was being acted upon in the log event)',
            'eventCode': 'Event Code',
        }
