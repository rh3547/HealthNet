"""
HealthNet Profile Forms
"""
from django import forms

from .models import User, Contact, Patient


# This form contains a text field for a username and a password field for a password.
# It is shown on the index page used to login to the system.
class IndexForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'required': 'true', 'placeholder': 'username', 'id': 'username-field'}),
            'password': forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'password', 'id': 'password-field'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstName', 'middleInitial', 'lastName', 'phoneNumber', 'street', 'city', 'state', 'zipcode', 'relation')
        labels = {
            'firstName': 'First Name',
            'middleInitial': 'M.I.',
            'lastName': 'Last Name',
            'phoneNumber': 'Phone Number',
            'street': 'Street Address',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zip Code',
            'relation': 'Relationship',
        }
        widgets = {
            'firstName': forms.TextInput(attrs={'required': 'true', 'id': 'firstName-field'}),
            'middleInitial': forms.TextInput(attrs={'required': 'true', 'id': 'middleInitial-field'}),
            'lastName': forms.TextInput(attrs={'required': 'true', 'id': 'lastName-field'}),
            'phoneNumber': forms.TextInput(attrs={'required': 'true', 'id': 'phoneNumber-field'}),
            'street': forms.TextInput(attrs={'required': 'true', 'id': 'street-field'}),
            'city': forms.TextInput(attrs={'required': 'true', 'id': 'city-field'}),
            'state': forms.TextInput(attrs={'required': 'true', 'id': 'state-field'}),
            'zipcode': forms.TextInput(attrs={'required': 'true', 'id': 'zipcode-field'}),
            'relation': forms.Select(attrs={'required': 'true', 'id': 'relation-field'}),
        }

    def __init__(self, *args, **kwargs):
        no_self = kwargs.pop('no_self', False)
        super(ContactForm, self).__init__(*args, **kwargs)
        NEW_RELATION_CHOICES = (
            ('ga', 'Guardian'),
            ('sp', 'Spouse'),
            ('fa', 'Father'),
            ('mo', 'Mother'),
            ('si', 'Sibling'),
            ('ch', 'Child'),
            ('ot', 'Other'),
        )
        if no_self:
            self.fields['relation'].choices = NEW_RELATION_CHOICES


class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('heightFeet', 'heightInches', 'weight', 'insuranceCompany', 'insuranceId', 'allergies', 'conditions', 'hospitalPref')
        labels = {
            'birthDate': 'Date of Birth',
            'heightFeet': 'Height Feet',
            'heightInches': 'Height Inches',
            'weight': 'Weight',
            'insuranceCompany': 'Insurance Company',
            'insuranceId': 'Insurance ID',
            'allergies': 'Allergies',
            'conditions': 'Medical Conditions',
            'hospitalPref': 'Preferred Hospital',
        }
        widgets = {
            'heightFeet': forms.NumberInput(attrs={'required': 'true', 'id': 'heightFeet-field'}),
            'heightInches': forms.NumberInput(attrs={'required': 'true', 'id': 'heightFeet-field'}),
            'weight': forms.NumberInput(attrs={'required': 'true', 'id': 'weight-field'}),
            'insuranceCompany': forms.TextInput(attrs={'required': 'true', 'id': 'insurance-company'}),
            'insuranceId': forms.TextInput(attrs={'required': 'true', 'id': 'insurance-id'}),
            'allergies': forms.Textarea(attrs={'required': 'true', 'id': 'allergies-field'}),
            'conditions': forms.Textarea(attrs={'required': 'true', 'id': 'conditions-field'}),
            'hospitalPref': forms.TextInput(attrs={'required': 'true', 'id': 'hospitalPref-field'}),
        }


class UserContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstName', 'middleInitial', 'lastName', 'phoneNumber', 'street', 'city', 'state', 'zipcode')
        labels = {
            'firstName': 'First Name',
            'middleInitial': 'M.I.',
            'lastName': 'Last Name',
            'phoneNumber': 'Phone Number',
            'street': 'Street Address',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zip Code',
        }
        widgets = {
            'firstName': forms.TextInput(attrs={'required': 'true', 'id': 'firstName-field'}),
            'middleInitial': forms.TextInput(attrs={'required': 'true', 'id': 'middleInitial-field'}),
            'lastName': forms.TextInput(attrs={'required': 'true', 'id': 'lastName-field'}),
            'phoneNumber': forms.TextInput(attrs={'required': 'true', 'id': 'phoneNumber-field'}),
            'street': forms.TextInput(attrs={'required': 'true', 'id': 'street-field'}),
            'city': forms.TextInput(attrs={'required': 'true', 'id': 'city-field'}),
            'state': forms.TextInput(attrs={'required': 'true', 'id': 'state-field'}),
            'zipcode': forms.TextInput(attrs={'required': 'true', 'id': 'zipcode-field'}),
        }


class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['isNew', 'accountType', 'prescriptions', 'user', 'birthDate']
        labels = {
            'heightFeet': 'Height Feet',
            'heightInches': 'Height Inches',
            'weight': 'Weight',
            'insuranceCompany': 'Insurance Company',
            'insuranceId': 'Insurance ID',
            'allergies': 'Allergies',
            'conditions': 'Medical Conditions',
            'hospitalPref': 'Preferred Hospital',
        }
        widgets = {
            'heightFeet': forms.NumberInput(attrs={'required': 'true', 'id': 'heightFeet-field'}),
            'heightInches': forms.NumberInput(attrs={'required': 'true', 'id': 'heightFeet-field'}),
            'weight': forms.NumberInput(attrs={'required': 'true', 'id': 'weight-field'}),
            'insuranceCompany': forms.TextInput(attrs={'required': 'true', 'id': 'insurance-company'}),
            'insuranceId': forms.TextInput(attrs={'required': 'true', 'id': 'insurance-id'}),
            'allergies': forms.Textarea(attrs={'required': 'true', 'id': 'allergies-field'}),
            'conditions': forms.Textarea(attrs={'required': 'true', 'id': 'conditions-field'}),
            'hospitalPref': forms.TextInput(attrs={'required': 'true', 'id': 'hospitalPref-field'}),
        }
