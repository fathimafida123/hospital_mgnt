from django.urls import path
from . import views

urlpatterns = [
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path(
    'doctor-appointments/',
    views.doctor_appointments,
    name='doctor_appointments'
),
path(
    'patient-appointments/',
    views.patient_appointments,
    name='patient_appointments'
),
]