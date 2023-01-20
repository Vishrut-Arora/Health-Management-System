from django.shortcuts import render

def doctorDashboard(request):
    context = {}
    return render(request, 'doctor.html', context)