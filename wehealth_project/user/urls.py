from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registration/', views.registration, name='user_registration'),
    path('getapproval/', views.get_approval, name='get_approval'),
    path('doctorDashboard/', include('doctor.urls'), name='doctor_dashboard'),
    path('patientDashboard/', include('patient.urls'), name='patient_dashboard'),
    path('organizationDashboard/', include('organization.urls'), name='organization_dashboard'),
    path('pharmacyDashboard/', include('pharmacy.urls'), name='pharmacy_dashboard'),
    path('insuranceDashboard/', include('insurance.urls'), name='insurance_dashboard'),
    path('hospitalDashboard/', include('hospital.urls'), name='hospital_dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)