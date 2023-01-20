from django.shortcuts import render
from doctor.models import Doctor
from user.models import User


def patientDashboard(request):
    context = {}
    print(request.POST)
    doctors = Doctor.objects.all()
    if(Doctor.objects.all()):
        print("ok")
    context['doctors'] = doctors
    print(context)
    return render(request, 'patient.html', context)