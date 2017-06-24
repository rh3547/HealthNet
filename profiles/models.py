"""
HealthNet Profile Models
"""
from django.db import models
from django.contrib.auth.models import User


# The User model represents the basic information for every Healthnet user.
class HealthNetUser(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('A', 'Admin'),
        ('N', 'Nurse'),
    )
    user = models.OneToOneField(User)
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='P')
    isNew = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


# The Patient model is a child of User and contains fields specific to a patient.
class Patient(HealthNetUser):
    birthDate = models.DateField()
    heightFeet = models.IntegerField()
    heightInches = models.IntegerField()
    weight = models.IntegerField()
    insuranceCompany = models.CharField(max_length=200)
    insuranceId = models.CharField(max_length=200)
    hospitalPref = models.CharField(max_length=200)
    allergies = models.TextField()
    conditions = models.TextField()
    prescriptions = models.TextField()

    def __str__(self):
        return self.user.username


# The Contact model contains contact information for a person.  Each User has many Contacts.
class Contact(models.Model):
    firstName = models.CharField(max_length=32)
    middleInitial = models.CharField(max_length=1)
    lastName = models.CharField(max_length=64)
    phoneNumber = models.CommaSeparatedIntegerField(max_length=11)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=12)
    zipcode = models.CharField(max_length=10)
    RELATION_CHOICES = (
        ('ga', 'Guardian'),
        ('sp', 'Spouse'),
        ('fa', 'Father'),
        ('mo', 'Mother'),
        ('si', 'Sibling'),
        ('ch', 'Child'),
        ('ot', 'Other'),
        ('se', 'Self'),
    )
    relation = models.CharField(max_length=2, choices=RELATION_CHOICES)
    user = models.ForeignKey(HealthNetUser)

    def __str__(self):
        return self.firstName
