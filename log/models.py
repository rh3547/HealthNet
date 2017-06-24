from django.db import models

class LogEvent(models.Model):
    source = models.CharField(max_length=64)
    action = models.CharField(max_length=64)
    eventCode = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.message
