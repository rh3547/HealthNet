from django.contrib import admin

from .models import Patient, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Login Credentials', {'fields': ['user.username']}),
    #     ('Medical information', {'fields': ['birthDate', 'height', 'weight', 'insurance', 'allergies',
    #      'conditions', 'prescriptions', 'hospitalPref']}),
    # ]
    inlines = [ContactInline]

    # search_fields = ['user.username']


admin.site.register(Patient, PatientAdmin)
