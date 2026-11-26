from django.shortcuts import render,redirect
from .forms import DoctorForm, PatientForm, AppointmentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def add_doctor(request):

    if request.method == "POST":
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')

    else:
        form = DoctorForm()

    return render(request, 'hospital/add_doctor.html', {'form': form})




def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')

    else:
        form = PatientForm()

    return render(request, 'hospital/add_patient.html', {'form': form})
@login_required
def book_appointment(request):

    patient = get_object_or_404(Patient, user=request.user)

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()

            return redirect('patient_dashboard')

    else:
        form = AppointmentForm()

    return render(request, 'hospital/book_appointment.html', {'form': form})
    return render(request, 'hospital/book_appointment.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Doctor, Appointment,Patient


@login_required
def doctor_appointments(request):
    doctor = get_object_or_404(Doctor, user=request.user)

    appointments = Appointment.objects.filter(doctor=doctor)

    return render(
        request,
        'hospital/doctor_appointments.html',
        {'appointments': appointments}
    )

@login_required
def patient_appointments(request):
    patient = get_object_or_404(Patient, user=request.user)

    appointments = Appointment.objects.filter(patient=patient)

    return render(
        request,
        'hospital/patient_appointments.html',
        {'appointments': appointments}
    )