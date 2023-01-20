from django.shortcuts import render

def hospitalDashboard(request):
    context = {}
    return render(request, 'hospital.html', context)