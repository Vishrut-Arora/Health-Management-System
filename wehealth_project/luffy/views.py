from django.shortcuts import render, redirect
import hashlib
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user.models import User

def adminLogin(request):
    context = {'error': False}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
  
        luffy = authenticate(username=username, password=password)

        if luffy is not None:
                login(request, luffy)
                return redirect('/')
        else:
            context['error'] = True
            return render(request, 'adminLogin.html', context)

    return render(request, 'adminLogin.html', context)


def adminSite(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    return render(request, 'adminSite.html', context)


def approveUser(request, auth_id):
    user = User.objects.get(auth_id=auth_id)
    user.is_authorized = True
    user.save()
    return redirect('/adminsite/')


def logOut(request):
    logout(request)
    return redirect('/')
    