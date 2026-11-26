from django.db import models
from django.conf import settings
# Create your models here.
class Doctor(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )

    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username
class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return f"{self.patient} - {self.doctor}"