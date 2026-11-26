from django.shortcuts import render,redirect
from .forms import Registration
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=="POST":
       form=Registration(request.POST)

       if form.is_valid():
           user=form.save(commit=False)
           user.role="patient"
           user.save()   

           return redirect("login")
    else:
        form=Registration()
    return render(request,'accounts/register.html',{'form':form}) 
@login_required      
def home(request):

    if request.user.role=='admin':
        return redirect('admin_dashboard')
    elif request.user.role=='doctor':
        return redirect('doctor_dashboard')
    elif request.user.role == 'patient':
        return redirect('patient_dashboard')
@login_required
def patient_dashboard(request):
    return render(request,'accounts/patient_dashboard.html')
@login_required
def doctor_dashboard(request):
    return render(request,'accounts/doctor_dashboard.html')