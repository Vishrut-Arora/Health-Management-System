from django.shortcuts import render

def pharmacyDashboard(request):
    context = {}
    return render(request, 'pharmacy.html', context)