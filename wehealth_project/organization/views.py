from django.shortcuts import render

def organizationDashboard(request):
    context = {}
    return render(request, 'organization.html', context)