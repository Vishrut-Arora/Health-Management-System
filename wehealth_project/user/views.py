from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User
import hashlib
from doctor.models import Doctor

def home(request):
    context = {'is_auth': False}
    
    if request.user.is_authenticated:
        context['is_auth'] = True
    
    if request.method == 'POST':
        return user_login(request)

    return render(request,'index.html', context)


def registration(request):
    
    content = {}
    
    if request.method == "POST":
        role = request.POST['role']
        auth_type = int(request.POST['type'])
        proof_number = int(request.POST['proof_number'])
        
        # check whether proof_number is validated by the admin
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # checking whether the user is approved or not by the admin
        test_user = User.objects.filter(auth_id=proof_number)
        
        if test_user.exists():
            test_user = test_user.get()
            
            # if the user is already registered then registration cannot happen again for the same credentials
            if test_user.is_registered:
                content['is_registered'] = True
                return render(request, 'user_registration.html', content)

            if test_user.is_authorized:
                
                if role == "1":
                    price = request.POST['doctor_price']
                    max_appointments = request.POST['doctor_max_appointments']
                
                    doctor = Doctor()
                    doctor.price = price
                    doctor.max_appointments = max_appointments
                    doctor.username = username

                    doctor.save()

                    # doctor
                    test_user.is_doctor = True
                    
                elif role == "2":
                    # patient
                    test_user.is_patient = True
                elif role == "3":
                    # pharmacy
                    test_user.is_pharmacy = True
                elif role == "4":
                    # insurance firms
                    test_user.is_insurance_firm = True
                elif role == "5":
                    # hospital
                    test_user.is_hospital = True
                
                test_user.type_auth = auth_type
                test_user.auth_id = proof_number
                test_user.username = username
                test_user.email = email
                test_user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                
                test_user.is_registered = True

                content['user_created'] = True

                test_user.save()
                return redirect('/')
            else:
                content['auth_not_done'] = True
        else:
            content['user_not_exists'] = True
            
    return render(request, 'user_registration.html', content)


def get_approval(request):
    content = {}
    if request.method == 'POST':
        auth_type = int(request.POST['type'])
        role_proof_image = request.POST['role_proof_image']
        proof_image = request.POST['proof_image']
        proof_number = int(request.POST['proof_number'])

        test_user = User.objects.filter(auth_id=proof_number)
        
        if not test_user.exists():
            user = User()
            user.type_auth = auth_type
            user.auth_image = proof_image
            user.auth_id = proof_number
            user.role_proof_image = role_proof_image

            user.save()

            return redirect('/')
        else:
            content['user_already_exist'] = True
        
    return render(request, 'getapproval.html', content)


def user_login(request):
    context = {}
    if request.method == 'POST':
        role = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        print(role)
        test_user = User.objects.filter(username=username)

        if test_user.exists():
            test_user = test_user.get()
            original_password = test_user.password

            if original_password == password:
                test_user.is_login = True
                context['username'] = username

                if role == '1':
                    # role should match
                    if not test_user.is_doctor:
                        context['role_wrong'] = True
                        return render(request, 'index.html', context)
                    # redirect to doctor page
                    return redirect('doctorDashboard/')
                    # return render(request, 'doctor.html', context)

                elif role == "2":
                    if not test_user.is_patient:
                        context['role_wrong'] = True
                        return render(request, 'index.html', context)
                    # redirect to patient page
                    return redirect('patientDashboard/')
                    # return render(request, 'patient.html', context)

                elif role == "3":
                    if not test_user.is_pharmacy:
                        context['role_wrong'] = True
                        return render(request, 'index.html', context)
                    # pharmacy
                    return redirect('pharmacyDashboard/')
                    # return render(request, 'pharmacy.html', context)
                elif role == "4":
                    if not test_user.is_insurance:
                        context['role_wrong'] = True
                        return render(request, 'index.html', context)
                    # insurance firms
                    return redirect('insuranceDashboard/')
                    # return render(request, 'insurance.html', context)
                elif role == "5":
                    if not test_user.is_hospital:
                        context['role_wrong'] = True
                        return render(request, 'index.html', context)
                    # hospital
                    return redirect('hospitalDashboard/')
                    # return render(request, 'hospital.html', context)
            else:
                context['password_wrong'] = True
        else:
            context['user_does_not_exists'] = True
        return render(request, 'index.html', context)
        

