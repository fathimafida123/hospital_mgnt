from django import forms
from .models import Doctor, Patient, Appointment
from accounts.models import CustomUser

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=["user","specialization","qualification",'phone']




class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['user', 'age', 'phone', 'address']
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'doctor',
            'appointment_date',
            'appointment_time',
            'reason'
        ]