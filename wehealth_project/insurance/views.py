from django.shortcuts import render

def insuranceDashboard(request):
    context = {}
    return render(request, 'insurance.html', context)